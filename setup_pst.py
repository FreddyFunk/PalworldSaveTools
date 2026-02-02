from __future__ import annotations
import os, sys, shutil, subprocess, threading, queue, argparse, re, platform, time
from pathlib import Path
from typing import Optional
PROJECT_DIR = Path(__file__).resolve().parent
VENV_DIR = PROJECT_DIR / '.pst_venv'
SENTINEL = VENV_DIR / '.ready'
USE_ANSI = True
if os.name == 'nt':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 5)
    except Exception:
        pass
def ansi(code: str) -> str:
    return code if USE_ANSI else ''
RESET, BOLD, GREEN, YELLOW, RED, CYAN, DIM = (ansi('\x1b[0m'), ansi('\x1b[1m'), ansi('\x1b[32m'), ansi('\x1b[33m'), ansi('\x1b[31m'), ansi('\x1b[36m'), ansi('\x1b[2m'))
def step_label(n: int, total: int, text: str) -> str:
    return f'[{n}/{total}]{text}'
def print_step_working(label: str):
    sys.stdout.write(f'{BOLD}{label}...{RESET}\r')
    sys.stdout.flush()
def print_ok(label: str):
    sys.stdout.write('\r' + ' ' * 120 + '\r')
    print(f'{BOLD}{label} {GREEN}OK{RESET}')
def print_fail(label: str):
    sys.stdout.write('\r' + ' ' * 120 + '\r')
    print(f'{BOLD}{label} {RED}FAILED{RESET}')
def reader_thread(proc: subprocess.Popen, q: queue.Queue):
    assert proc.stdout is not None
    try:
        for raw in proc.stdout:
            q.put(raw.rstrip('\n'))
    except Exception:
        pass
    finally:
        try:
            proc.stdout.close()
        except Exception:
            pass
        q.put(None)
def progress_bar(pct: int, width: int=30) -> str:
    filled = int(pct / 100.0 * width)
    return '[' + '#' * filled + '-' * (width - filled) + ']'
_SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
def run_and_watch(cmd, cwd=None, env=None):
    filter_keys = ('Collecting', 'Downloading', '%', 'Building wheel for', 'Installing collected packages', 'Successfully installed', 'ERROR', 'Failed')
    cmd_list = list(map(str, cmd))
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, cwd=cwd, env=env)
    q: queue.Queue = queue.Queue()
    threading.Thread(target=reader_thread, args=(proc, q), daemon=True).start()
    progress_pct, last_shown_msg = (None, None)
    try:
        while True:
            try:
                line = q.get(timeout=0.08)
            except queue.Empty:
                line = None
            if line is None:
                if proc.poll() is not None and q.empty():
                    break
                continue
            s = line.rstrip()
            m = re.search('(\\d{1,3})\\s*%+', s)
            pct = int(m.group(1)) if m else None
            if pct is not None:
                progress_pct = max(0, min(100, pct))
            if any((key in s for key in filter_keys)) or progress_pct is not None:
                if s != last_shown_msg:
                    if progress_pct is not None:
                        sys.stdout.write(f'\r{CYAN}{progress_bar(progress_pct, width=28)} {progress_pct:3d}%{RESET}')
                        sys.stdout.flush()
                    else:
                        sys.stdout.write('\r' + ' ' * 120 + '\r')
                        print(f'{CYAN}> {s}{RESET}')
                    last_shown_msg = s
    finally:
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    return proc.wait()
def run_apt_install(packages, label='Installing'):
    total = len(packages)
    cmd = ['sudo', 'apt-get', 'install', '-y', '-qq'] + packages
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    q: queue.Queue = queue.Queue()
    threading.Thread(target=reader_thread, args=(proc, q), daemon=True).start()
    installed_count = 0
    spinner_idx = 0
    current_pct = 0
    error_keywords = ('error', 'failed', 'unable', 'cannot', 'permission denied', 'could not')
    try:
        while True:
            try:
                line = q.get(timeout=0.08)
            except queue.Empty:
                line = None
            if line is None:
                if proc.poll() is not None and q.empty():
                    break
            s = line.rstrip() if line else ''
            if 'Setting up' in s or 'Unpacking' in s:
                installed_count += 1
                current_pct = min(100, int(installed_count / total * 100)) if total > 0 else 100
            if any((err in s.lower() for err in error_keywords)):
                sys.stdout.write('\r' + ' ' * 120 + '\r')
                print(f'{RED}> {s}{RESET}')
            spinner_idx = (spinner_idx + 1) % len(_SPINNER_FRAMES)
            if current_pct > 0:
                sys.stdout.write(f'\r{CYAN}{progress_bar(current_pct, width=28)} {label} ({installed_count}/{total}) {_SPINNER_FRAMES[spinner_idx]}{RESET}')
            else:
                sys.stdout.write(f'\r{CYAN}{label}... {_SPINNER_FRAMES[spinner_idx]}{RESET}')
            sys.stdout.flush()
    finally:
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    return proc.wait()
def nuke_build_artifacts():
    print_step_working('Cleaning environment')
    for item in ['build', 'dist']:
        path = PROJECT_DIR / item
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)
    for p in PROJECT_DIR.rglob('*.egg-info'):
        if p.is_dir():
            shutil.rmtree(p, ignore_errors=True)
    for p in PROJECT_DIR.rglob('__pycache__'):
        if p.is_dir():
            shutil.rmtree(p, ignore_errors=True)
    print_ok('Environment cleaned')
def venv_python_path() -> Path:
    if os.name == 'nt':
        return VENV_DIR / 'Scripts' / 'python.exe'
    return VENV_DIR / 'bin' / 'python'
def ensure_python_venv_installed():
    if os.name != 'posix' or platform.system() != 'Linux':
        return True
    is_debian_based = False
    try:
        result = subprocess.run(['which', 'apt'], capture_output=True, timeout=5)
        is_debian_based = result.returncode == 0
    except Exception:
        pass
    if not is_debian_based:
        return True
    py_version = f'python{sys.version_info.major}.{sys.version_info.minor}'
    print(f'{DIM}Detected Python: {py_version} on Debian/Ubuntu-based system{RESET}')
    test_venv = PROJECT_DIR / '.test_venv'
    if test_venv.exists():
        shutil.rmtree(test_venv, ignore_errors=True)
    try:
        result = subprocess.run([sys.executable, '-m', 'venv', str(test_venv)], capture_output=True, timeout=30)
        if result.returncode == 0:
            shutil.rmtree(test_venv, ignore_errors=True)
            return True
    except Exception:
        pass
    finally:
        if test_venv.exists():
            shutil.rmtree(test_venv, ignore_errors=True)
    packages_to_install = []
    for pkg in [f'{py_version}-venv', f'{py_version}-dev', 'python3-venv', 'python3-pip', 'python3-dev', 'python3-tk']:
        try:
            result = subprocess.run(['dpkg', '-s', pkg], capture_output=True, timeout=5)
            if result.returncode != 0:
                packages_to_install.append(pkg)
        except Exception:
            packages_to_install.append(pkg)
    packages_to_install = list(dict.fromkeys(packages_to_install))
    if not packages_to_install:
        return True
    print(f"{YELLOW}Missing required packages: {', '.join(packages_to_install)}{RESET}")
    print_step_working('Installing system packages')
    try:
        result = run_apt_install(packages_to_install, 'Installing')
        if result == 0:
            print_ok('System packages installed')
            return True
        else:
            print_fail('System package installation failed')
            print(f"{RED}Please run manually: sudo apt install -y {' '.join(packages_to_install)}{RESET}")
            return False
    except Exception as e:
        print_fail(f'System package installation: {e}')
        return False
def nuke_venv():
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        if SENTINEL.exists():
            SENTINEL.unlink(missing_ok=True)
def ensure_qt_dependencies():
    if os.name != 'posix' or platform.system() != 'Linux':
        return True
    is_debian_based = False
    try:
        result = subprocess.run(['which', 'apt'], capture_output=True, timeout=5)
        is_debian_based = result.returncode == 0
    except Exception:
        pass
    if not is_debian_based:
        return True
    qt_packages = ['libxcb-cursor0', 'libxcb-xinerama0', 'libxcb-xkb1', 'libxcb-icccm4', 'libxcb-image0', 'libxcb-keysyms1', 'libxcb-randr0', 'libxcb-render-util0', 'libxcb-xfixes0', 'libxcb-shape0', 'libxkbcommon-x11-0', 'libfontconfig1', 'libgl1']
    packages_to_install = []
    for pkg in qt_packages:
        try:
            result = subprocess.run(['dpkg', '-s', pkg], capture_output=True, timeout=5)
            if result.returncode != 0:
                packages_to_install.append(pkg)
        except Exception:
            packages_to_install.append(pkg)
    if not packages_to_install:
        return True
    print(f"{YELLOW}Missing Qt dependencies: {', '.join(packages_to_install)}{RESET}")
    print_step_working('Installing Qt dependencies')
    try:
        result = run_apt_install(packages_to_install, 'Installing Qt')
        if result == 0:
            print_ok('Qt dependencies installed')
            return True
        else:
            print_fail('Qt dependency installation failed')
            print(f"{RED}Please run manually: sudo apt install -y {' '.join(packages_to_install)}{RESET}")
            return False
    except Exception as e:
        print_fail(f'Qt dependency installation: {e}')
        return False
def main():
    msg = "\n  ___      _                _    _ ___              _____         _    \n | _ \\__ _| |_ __ _____ _ _| |__| / __| __ ___ ____|_   _|__  ___| |___\n |  _/ _` | \\ V  V / _ \\ '_| / _` \\__ \\/ _` \\ V / -_)| |/ _ \\/ _ \\(_-<\n |_| \\__,_|_|\\_/\\_/\\___/_| |_\\__,_|___/\\__,_|\\_/\\___||_|\\___/\\___/_/__/\n    "
    print(msg)
    if not SENTINEL.exists():
        nuke_build_artifacts()
        if not VENV_DIR.exists():
            if not ensure_python_venv_installed():
                print_fail(step_label(1, 3, 'python3-venv setup failed'))
                return
            print_step_working(step_label(1, 3, 'Creating Virtual Environment'))
            venv_result = subprocess.run([sys.executable, '-m', 'venv', str(VENV_DIR)])
            if venv_result.returncode != 0:
                print_fail(step_label(1, 3, 'Venv creation failed'))
                nuke_venv()
                return
            print_ok(step_label(1, 3, 'Venv created'))
        vpy = venv_python_path()
        print_step_working(step_label(2, 3, 'Updating Dependencies'))
        ret = run_and_watch([str(vpy), '-m', 'pip', 'install', 'pip==24.3.1', 'setuptools==75.6.0', 'wheel', 'numpy==2.1.3', 'PySide6-Essentials', 'shiboken6', 'packaging'])
        if ret == 0:
            SENTINEL.touch()
            print_ok(step_label(2, 3, 'Dependencies updated'))
        else:
            print_fail(step_label(2, 3, 'Dependency update failed'))
            nuke_venv()
            return
    vpy = venv_python_path()
    start_py = PROJECT_DIR / 'start.py'
    if start_py.exists():
        if SENTINEL.exists():
            print(f"{DIM}{step_label(3, 3, 'Environment ready,bypassing checks')}{RESET}")
        if not ensure_qt_dependencies():
            print_fail(step_label(3, 3, 'Qt dependencies check failed'))
            return
        print(f"{BOLD}{step_label(3, 3, 'Launching Application')}{RESET}")
        subprocess.call([str(vpy), str(start_py)])
if __name__ == '__main__':
    main()