#!/usr/bin/env python3
from __future__ import annotations
import os
import sys
import shutil
import subprocess
import threading
import queue
import time
from pathlib import Path
PROJECT_DIR = Path(__file__).resolve().parent
USE_ANSI = True
if os.name == "nt":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 5)
    except Exception:
        pass
def ansi(code: str) -> str:
    return code if USE_ANSI else ""
RESET = ansi("\x1b[0m")
BOLD = ansi("\x1b[1m")
GREEN = ansi("\x1b[32m")
YELLOW = ansi("\x1b[33m")
RED = ansi("\x1b[31m")
CYAN = ansi("\x1b[36m")
DIM = ansi("\x1b[2m")
def step_label(n: int, total: int, text: str) -> str:
    return f"[{n}/{total}] {text}"
def print_step_working(label: str):
    sys.stdout.write(f"{BOLD}{label}...{RESET}\r")
    sys.stdout.flush()
def print_ok(label: str):
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"{BOLD}{label} {GREEN}OK{RESET}")
def print_fail(label: str):
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"{BOLD}{label} {RED}FAILED{RESET}")
def print_info(label: str):
    print(f"{BOLD}{label}{RESET}")
def print_small(msg: str):
    print(f"{DIM}{msg}{RESET}")
def reader_thread(proc: subprocess.Popen, q: queue.Queue):
    assert proc.stdout is not None
    try:
        for raw in proc.stdout:
            q.put(raw.rstrip("\n"))
    except Exception:
        pass
    finally:
        proc.stdout.close()
        q.put(None)
def run_and_watch(cmd, cwd=None, env=None, filter_keys=None, update_callback=None):
    if filter_keys is None:
        filter_keys = ("Collecting", "Downloading", "%", "Building wheel for", "Installing collected packages", "Successfully installed", "ERROR", "Failed", "Cloning", "Running command git")
    proc = subprocess.Popen(
        list(map(str, cmd)),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        cwd=cwd,
        env=env,
    )
    q: queue.Queue = queue.Queue()
    t = threading.Thread(target=reader_thread, args=(proc, q), daemon=True)
    t.start()
    progress_pct = None
    last_shown_msg = None
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
            if line is None:
                continue
            s = line.strip()
            show = False
            for key in filter_keys:
                if key in s:
                    show = True
                    break
            pct = None
            import re
            m = re.search(r"(\d{1,3})%+", s)
            if m:
                try:
                    pct = int(m.group(1))
                except Exception:
                    pct = None
            if pct is not None:
                progress_pct = max(0, min(100, pct))
            if show or pct is not None:
                if s != last_shown_msg:
                    if update_callback:
                        update_callback(s, progress_pct)
                    else:
                        if progress_pct is not None:
                            bar = progress_bar(progress_pct, width=28)
                            sys.stdout.write(f"\r{CYAN}{bar} {progress_pct:3d}%{RESET}")
                            sys.stdout.flush()
                            if "Downloading" not in s and "Collecting" not in s:
                                 progress_pct = None
                        else:
                            sys.stdout.write("\r" + " " * 80 + "\r")
                            print(f"{CYAN}> {s}{RESET}")
                    last_shown_msg = s
    finally:
        if not update_callback:
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.flush()
    return proc.wait()
def progress_bar(pct: int, width: int = 30) -> str:
    filled = int((pct / 100.0) * width)
    empty = width - filled
    return "[" + "#" * filled + "-" * empty + "]"
def find_system_python() -> str:
    for name in ("python3", "python"):
        p = shutil.which(name)
        if p:
            return p
    return sys.executable
VENV_DIR = PROJECT_DIR / "pst_venv"
def venv_python_path() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"
def check_package_installed(venv_py: Path, package_name: str) -> bool:
    try:
        result = subprocess.run(
            [str(venv_py), "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False
def create_venv():
    print_step_working(step_label(1, 4, "Creating virtual environment"))
    if VENV_DIR.exists():
        print_small(f"Venv exists: {VENV_DIR}")
        print_ok(step_label(1, 4, "Virtual environment already exists"))
        return True
    creator = find_system_python()
    rc = subprocess.call([creator, "-m", "venv", str(VENV_DIR)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if rc != 0:
        print_fail(step_label(1, 4, "Creating virtual environment"))
        return False
    print_ok(step_label(1, 4, "Virtual environment created"))
    return True
def ensure_packaging_tools(venv_py: Path):
    print_step_working(step_label(2, 4, "Upgrading pip / setuptools / wheel"))
    rc = run_and_watch([str(venv_py), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
                       filter_keys=("Installing collected packages", "Successfully installed", "ERROR", "Failed", "%"))
    if rc == 0:
        print_ok(step_label(2, 4, "Pip / tools upgraded"))
    else:
        print_fail(step_label(2, 4, "Upgrading pip / setuptools / wheel"))
        print_small("Continuing (pip upgrade failure may still allow installs).")
def install_packaging(venv_py: Path):
    if check_package_installed(venv_py, "packaging"):
        print_info("Packaging already installed")
        return True
    print_step_working(step_label(3, 4, "Installing packaging"))
    rc = run_and_watch([str(venv_py), "-m", "pip", "install", "packaging"],
                       filter_keys=("Installing collected packages", "Successfully installed", "ERROR", "Failed", "%"))
    if rc == 0:
        print_ok(step_label(3, 4, "Packaging installed"))
        return True
    else:
        print_fail(step_label(3, 4, "Installing packaging"))
        return False

def install_pyside(venv_py: Path):
    if check_package_installed(venv_py, "pyside6-essentials"):
        print_info("PySide6 Essentials already installed")
        return True
    print_step_working(step_label(4, 4, "Installing PySide6 Essentials"))
    rc = run_and_watch([str(venv_py), "-m", "pip", "install", "pyside6-essentials"],
                       filter_keys=("Installing collected packages", "Successfully installed", "ERROR", "Failed", "%"))
    if rc == 0:
        print_ok(step_label(4, 4, "PySide6 Essentials installed"))
        return True
    else:
        print_fail(step_label(4, 4, "Installing PySide6 Essentials"))
        return False
def main():
    print()
    print(f"{BOLD}##################################{RESET}")
    print(f"{BOLD}#   Palworld Save Tools Setup    #{RESET}")
    print(f"{BOLD}##################################{RESET}")
    print()
    ok = create_venv()
    if not ok:
        sys.exit(1)
    venv_py = venv_python_path()
    if not venv_py.exists():
        creator = find_system_python()
        rc = subprocess.call([creator, "-m", "venv", str(VENV_DIR)])
        if rc != 0:
            print_fail("Failed to create venv with system python")
            sys.exit(2)
    ensure_packaging_tools(venv_py)
    packaging_ok = install_packaging(venv_py)
    if not packaging_ok:
        print_small("Packaging installation failed.")
        sys.exit(3)
    deps_ok = install_pyside(venv_py)
    if not deps_ok:
        print_small("PySide6 Essentials installation failed; you can re-run the script to retry.")
        sys.exit(3)
    print_info("Launching start.py...")
    rc = subprocess.call([str(venv_py), str(PROJECT_DIR / "start.py")])
    sys.exit(rc)
if __name__ == "__main__":
    main()
