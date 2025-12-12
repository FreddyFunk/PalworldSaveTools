import os, sys, shutil, subprocess, re, tempfile, urllib.request, zipfile, ctypes
from pathlib import Path
import importlib.util
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
def unlock_self_folder():
    print(f"Attempting to unlock the folder...")
    folder=os.path.dirname(os.path.abspath(sys.argv[0]))
    script=(
        f"$target=\"{folder}\"\n"
        "$p=Get-Process\n"
        "foreach($x in $p){try{if($x.Path -and $x.Path.StartsWith($target)){Stop-Process -Id $x.Id -Force -ErrorAction SilentlyContinue}}catch{}}\n"
        "foreach($x in $p){try{$m=$x.Modules|Where-Object{$_.FileName -and $_.FileName.StartsWith($target)};if($m.Count -gt 0){Stop-Process -Id $x.Id -Force -ErrorAction SilentlyContinue}}catch{}}\n"
        "exit\n"
    )
    tmp=tempfile.NamedTemporaryFile(delete=False,suffix=".ps1")
    tmp.write(script.encode())
    tmp.close()
    si=subprocess.STARTUPINFO()
    si.dwFlags=subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen(["powershell","-WindowStyle","Hidden","-ExecutionPolicy","Bypass","-File",tmp.name],startupinfo=si,creationflags=subprocess.CREATE_NO_WINDOW)
    print("Operation completed.")
    os._exit(0)
def hide_console():
    return
    if sys.platform == "win32":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)
def show_console():
    return
    if sys.platform == "win32":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 5)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/deafdudecomputers/PalworldSaveTools/main/Assets/common.py"
GITHUB_LATEST_ZIP = "https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest"
UPDATE_CACHE=None
def get_cached_update_info():
    global UPDATE_CACHE
    if UPDATE_CACHE is None:
        UPDATE_CACHE=check_github_update(force_test=False)
    return UPDATE_CACHE
def check_github_update(auto_download=False, download_folder="PST_update", force_test=False):
    try:
        r=urllib.request.urlopen(GITHUB_RAW_URL,timeout=5)
        content=r.read().decode("utf-8")
        match=re.search(r'APP_VERSION\s*=\s*"([^"]+)"',content)
        latest=match.group(1) if match else None
        local,_=get_versions()
        if force_test: local="0.0.1"
        if latest:
            local_tuple=tuple(int(x) for x in local.split("."))
            latest_tuple=tuple(int(x) for x in latest.split("."))
            if local_tuple>=latest_tuple:
                print(f"{GREEN_FONT}{t('update.latest_version')} {local}{RESET_FONT}")
                return True,latest
            print(f"{YELLOW_FONT}{t('update.new_available')}{RESET_FONT}")
            print(f"{YELLOW_FONT}{t('update.local')}: {local}  {t('update.latest')}: {latest}{RESET_FONT}")
            print(f"{BLUE_FONT}{t('update.download_here')}{RESET_FONT}")
            print(f"{BLUE_FONT}{GITHUB_LATEST_ZIP}{RESET_FONT}")
            return False,latest
        print(f"{RED_FONT}{t('update.parse_error')}{RESET_FONT}")
        return True,None
    except Exception as e:
        print(f"{RED_FONT}{t('update.failed')} {e}{RESET_FONT}")
        return True,None
def center_window(win):
    win.update_idletasks()
    w, h = win.winfo_width(), win.winfo_height()
    ws, hs = win.winfo_screenwidth(), win.winfo_screenheight()
    x, y = (ws - w) // 2, (hs - h) // 2
    win.geometry(f'{w}x{h}+{x}+{y}')
def is_frozen():
    return getattr(sys, 'frozen', False)
def get_assets_path():
    if is_frozen():
        return os.path.join(os.path.dirname(sys.executable), "Assets")
    else:
        return os.path.join(os.path.dirname(__file__), "Assets")
if getattr(sys,"frozen",False):
    exe_dir=os.path.dirname(sys.executable)
    assets_path=os.path.join(exe_dir,"Assets")
    if assets_path not in sys.path:
        sys.path.insert(0,assets_path)
def setup_import_paths():
    assets_path = get_assets_path()
    if assets_path not in sys.path:
        sys.path.insert(0, assets_path)
    subdirs = ['palworld_coord', 'palworld_save_tools', 'palworld_xgp_import', 'resources']
    for subdir in subdirs:
        subdir_path = os.path.join(assets_path, subdir)
        if os.path.exists(subdir_path) and subdir_path not in sys.path:
            sys.path.insert(0, subdir_path)
setup_import_paths()
try:
    from i18n import init_language, t, set_language, get_language, load_resources
except Exception:
    def t(key, **fmt):
        return key.format(**fmt) if fmt else key
    def init_language(default_lang: str = "zh_CN"):
        pass
    def set_language(lang: str):
        pass
    def get_language():
        return "zh_CN"
    def load_resources(lang: str | None = None):
        pass
class LazyImporter:      
    def __init__(self):
        self._modules = {}
        self._common_funcs = None     
    def _try_import(self, module_name):
        import importlib
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
            self._modules[module_name] = sys.modules[module_name]
            return self._modules[module_name]
        try:
            module = importlib.import_module(module_name)
            self._modules[module_name] = module
            return module
        except ImportError:
            pass
        try:
            full_module_name = f"Assets.{module_name}"
            if full_module_name in sys.modules:
                importlib.reload(sys.modules[full_module_name])
                self._modules[module_name] = sys.modules[full_module_name]
                return self._modules[module_name]
            module = importlib.import_module(full_module_name)
            self._modules[module_name] = module
            return module
        except ImportError:
            pass
        try:
            assets_path = get_assets_path()
            module_file = os.path.join(assets_path, f"{module_name}.py")
            if os.path.exists(module_file):
                spec = importlib.util.spec_from_file_location(module_name, module_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    self._modules[module_name] = module
                    return module
        except Exception:
            pass
        raise ImportError(t("error.module") + f" {module_name}")
    def get_module(self, module_name):
        return self._try_import(module_name)      
    def get_function(self, module_name, function_name):
        module = self.get_module(module_name)
        return getattr(module, function_name)      
    def get_common_functions(self):
        if self._common_funcs is not None:
            return self._common_funcs         
        try:
            common_module = self._try_import('common')
            self._common_funcs = {
                'ICON_PATH': getattr(common_module, 'ICON_PATH', 'Assets/resources/pal.ico'),
                'get_versions': getattr(common_module, 'get_versions', lambda: ("Unknown", "Unknown")),
                'open_file_with_default_app': getattr(common_module, 'open_file_with_default_app', lambda x: None)
            }
        except ImportError:
            self._common_funcs = {
                'ICON_PATH': 'Assets/resources/pal.ico',
                'get_versions': lambda: ("Unknown", "Unknown"),
                'open_file_with_default_app': lambda x: None
            }         
        return self._common_funcs
lazy_importer = LazyImporter()
common_funcs = lazy_importer.get_common_functions()
ICON_PATH = common_funcs['ICON_PATH']
get_versions = common_funcs['get_versions']
open_file_with_default_app = common_funcs['open_file_with_default_app']
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def is_frozen():
    return getattr(sys, 'frozen', False)
def get_python_executable():
    if is_frozen():
        return sys.executable
    else:
        return sys.executable
RED_FONT = "\033[91m"
BLUE_FONT = "\033[94m"
GREEN_FONT = "\033[92m"
YELLOW_FONT= "\033[93m"
PURPLE_FONT = "\033[95m"
RESET_FONT = "\033[0m"
original_executable = sys.executable
def set_console_title(title): os.system(f'title {title}') if sys.platform == "win32" else print(f'\033]0;{title}\a', end='', flush=True)
def setup_environment():
    if sys.platform != "win32":
        try:
            import resource
            resource.setrlimit(resource.RLIMIT_NOFILE, (65535, 65535))
        except ImportError:
            pass
    os.system('cls' if os.name == 'nt' else 'clear')
    os.makedirs("PalworldSave/Players", exist_ok=True)
try:
    columns = os.get_terminal_size().columns
except OSError:
    columns = 80
def center_text(text):
    return "\n".join(line.center(columns) for line in text.splitlines())
def run_tool(choice):
    def import_and_call(module_name, function_name, *args):
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        func = lazy_importer.get_function(module_name, function_name)
        return func(*args) if args else func()
    tool_lists = [
        [
            lambda: import_and_call("convert_level_location_finder", "convert_level_location_finder", "json"),
            lambda: import_and_call("convert_level_location_finder", "convert_level_location_finder", "sav"),
            lambda: import_and_call("convert_players_location_finder", "convert_players_location_finder", "json"),
            lambda: import_and_call("convert_players_location_finder", "convert_players_location_finder", "sav"),
            lambda: import_and_call("game_pass_save_fix", "game_pass_save_fix"),
            lambda: import_and_call("convertids", "convert_steam_id"),
        ],
        [
            lambda: import_and_call("all_in_one_tools", "all_in_one_tools"),
            lambda: import_and_call("slot_injector", "slot_injector"),
            lambda: import_and_call("modify_save", "modify_save"),
            lambda: import_and_call("character_transfer", "character_transfer"),
            lambda: import_and_call("fix_host_save", "fix_host_save"),
            lambda: import_and_call("restore_map", "restore_map"),
        ]
    ]
    try:
        category_index, tool_index = choice
        return tool_lists[category_index][tool_index]()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"{t('error.tool')} {e}")
converting_tool_keys = [
    "tool.convert.level.to_json",
    "tool.convert.level.to_sav",
    "tool.convert.players.to_json",
    "tool.convert.players.to_sav",
    "tool.convert.gamepass.steam",
    "tool.convert.steamid",
]
management_tool_keys = [
    "tool.deletion",
    "tool.slot_injector",
    "tool.modify_save",
    "tool.character_transfer",
    "tool.fix_host_save",
    "tool.restore_map",
]
class MenuGUI(ctk.CTk):
    def tk_error_handler(self, exc, val, tb):
        from traceback import format_exception
        err_type=exc.__name__
        err_msg=str(val)
        full_trace="".join(format_exception(exc,val,tb))
        show_console()
        print("\n=== PST START ERROR ===\n")
        print(full_trace)
        print(f"[ERROR TYPE] {err_type}")
        print(f"[DESCRIPTION] {err_msg}")
        print("\n=== PST END ERROR ===\n")
        messagebox.showerror("PST Error",f"[ERROR TYPE] {err_type}\n[DESCRIPTION] {err_msg}\n\n========================\nFull Traceback Logged\n========================")
        hide_console()
    def __init__(self):
        super().__init__()
        self.running = True 
        self.report_callback_exception = self.tk_error_handler
        self.geometry("850x650")
        self.resizable(True, True)
        tools_version, _ = get_versions()
        self.title(t("app.title", version=tools_version))
        try:
            if os.name == 'nt' and os.path.exists(ICON_PATH):
                self.iconbitmap(ICON_PATH)
        except Exception as e:
            pass
        self.info_labels = []
        self.version_labels = []
        self.category_frames = []
        self.tool_buttons = []
        self.lang_combo = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.setup_ui()
        center_window(self)
    def _create_tool_section(self, parent_frame, col_idx, categories, start_idx=0):
        current_row = 0
        BUTTON_WIDTH = 300 
        for idx, (title, tools) in enumerate(categories, start=start_idx):
            cat_frame = ctk.CTkFrame(parent_frame, fg_color="transparent")
            cat_frame.grid(row=current_row, column=col_idx, padx=10, pady=10, sticky="nsew") 
            cat_frame.grid_columnconfigure(0, weight=1)
            lbl = ctk.CTkLabel(cat_frame, text=t(title), font=("Segoe UI", 16, "bold"), text_color="#A9A9A9")
            lbl.grid(row=0, column=0, pady=10)
            self.category_frames.append((lbl, title))
            for btn_i, tool_key in enumerate(tools):
                tool_idx = (idx, btn_i)
                btn_fg_color = None
                btn_hover_color = None
                btn = ctk.CTkButton(
                    cat_frame, 
                    text=t(tool_key), 
                    height=35,
                    width=BUTTON_WIDTH,
                    font=("Segoe UI", 13),
                    fg_color=btn_fg_color,
                    hover_color=btn_hover_color,
                    command=lambda idx=tool_idx: self.run_tool(idx)
                )
                btn.grid(row=btn_i+1, column=0, padx=0, pady=5) 
                self.tool_buttons.append((btn, tool_key))
            current_row += 1
    def setup_ui(self):
        tools_version, game_version = get_versions()
        import webbrowser
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, padx=20, pady=(15, 0), sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=0)
        header_frame.grid_columnconfigure(2, weight=1)
        logo_path = os.path.join("Assets", "resources", "PalworldSaveTools.png")
        if os.path.exists(logo_path):
            pil_img = Image.open(logo_path)
            ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(300, 75))
            logo_label = ctk.CTkLabel(header_frame, text="", image=ctk_img)
            logo_label.grid(row=0, column=1, pady=(5, 5), sticky="n")
        else:
            logo_text = "PALWORLD SAVE TOOLS"
            logo_label = ctk.CTkLabel(header_frame, text=logo_text, font=("Segoe UI", 24, "bold"), text_color="#3B8ED0")
            logo_label.grid(row=0, column=1, pady=(5, 5), sticky="n")
        self.lang_combo = ctk.CTkOptionMenu(
            header_frame,
            width=120,
            values=[],
            command=self.on_language_change_cmd
        )
        self.lang_combo.place(relx=1.0, rely=0.0, x=-10, y=5, anchor="ne")
        info_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        info_frame.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="ew")
        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=0)
        info_frame.grid_columnconfigure(2, weight=1)
        update_info = get_cached_update_info()
        status_text = t("app.subtitle", game_version=game_version)
        status_color = "#2CC985"
        status_label = ctk.CTkLabel(info_frame, text=status_text, text_color=status_color,
                                     font=("Segoe UI", 13, "bold"), justify="center", wraplength=780)
        status_label.grid(row=0, column=1, padx=10, pady=5)
        self.info_labels.append((status_label, "app.subtitle", {"game_version": game_version}))
        import webbrowser
        update_info=get_cached_update_info()
        if update_info:
            has_update,latest_version=update_info
            tools_version,_=get_versions()
            self.version_frame=ctk.CTkFrame(self, fg_color="transparent")
            self.version_frame.place(x=10,y=10)
            latest_text_key = 'update.latest'
            latest_text_fmt = {'version': latest_version}
            self.latest_label=ctk.CTkLabel(self.version_frame,text=f"{t(latest_text_key)}: {latest_version}",fg_color="transparent",text_color="white",font=("Consolas",12,"bold"))
            self.latest_label.pack(anchor="w")
            self.version_labels.append((self.latest_label, latest_text_key, latest_text_fmt))
            separator=ctk.CTkFrame(self.version_frame,height=1,fg_color="#666",corner_radius=0)
            separator.pack(fill="x",pady=1)
            current_text_key = 'update.current'
            current_text_fmt = {'version': tools_version}
            self.current_label=ctk.CTkLabel(self.version_frame,text=f"{t(current_text_key)}: {tools_version}",fg_color="transparent",text_color="white",font=("Consolas",12,"bold"))
            self.current_label.pack(anchor="w")
            self.current_label.bind("<Button-1>",lambda e:webbrowser.open("https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest"))
            self.version_labels.append((self.current_label, current_text_key, current_text_fmt))
            if not has_update:
                def pulse_current():
                    if not self.running: return
                    self.latest_label.configure(text_color="red" if self.latest_label.cget("text_color")=="white" else "white")
                    self.latest_label.after(700,pulse_current)
                pulse_current()
        critical_warnings = [
            ("notice.backup", {}, "#FF5555", ("Segoe UI", 11)),
            ("notice.patch", {"game_version": game_version}, "#FF5555", ("Segoe UI", 11)),
            ("notice.errors", {}, "#FF5555", ("Segoe UI", 11)),
        ]
        for i, (key, fmt, color, font) in enumerate(critical_warnings):
            f_family = font[0]
            f_size = font[1]
            f_weight = "bold" if len(font) > 2 and "bold" in font else "normal"
            label = ctk.CTkLabel(info_frame, text=t(key, **fmt), text_color=color,
                                     font=(f_family, f_size, f_weight), justify="center", wraplength=780)
            label.grid(row=i+1, column=1, padx=10, pady=1)
            self.info_labels.append((label, key, fmt))
        scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        left_categories = [
            ("cat.converting", converting_tool_keys),
        ]
        right_categories = [
            ("cat.management", management_tool_keys)
        ]
        self._create_tool_section(scroll_frame, 0, left_categories, 0)
        self._create_tool_section(scroll_frame, 1, right_categories, 1)
        self.refresh_texts()
    def on_language_change_cmd(self, choice):
        sel = choice
        lang_map = {t(f'lang.{code}'): code for code in ["zh_CN","en_US","ru_RU","fr_FR","es_ES","de_DE","ja_JP","ko_KR"]}
        lang = lang_map.get(sel, "zh_CN")
        set_language(lang)
        load_resources(lang)
        self.refresh_texts()
    def get_tool_name(self, choice):
        try:
            category_index, tool_index = choice
            if category_index == 0:
                key = converting_tool_keys[tool_index]
            elif category_index == 1:
                key = management_tool_keys[tool_index]
            else:
                key = str(choice)
            return t(key)
        except Exception:
            return str(choice)
    def run_tool(self, choice):
        tool_name = self.get_tool_name(choice)
        print(t('status.open', name=tool_name))
        self.withdraw()
        try:
            tool_window = run_tool(choice)
            if tool_window: tool_window.wait_window()
        except Exception:
            pass
        self.refresh_texts()
        print(t('status.close', name=tool_name))
        self.deiconify()
    def refresh_texts(self):
        tools_version,_=get_versions()
        self.title(t("app.title", version=tools_version))
        for label, key, fmt in self.version_labels:
            if key == 'update.latest':
                _, version = get_cached_update_info()
                text = f"{t(key)}: {version}"
            elif key == 'update.current':
                version, _ = get_versions()
                text = f"{t(key)}: {version}"
            else:
                text = t(key, **fmt)
            current_color = label.cget("text_color")
            label.configure(text=text)
            label.configure(text_color=current_color)
        for label, key, fmt in self.info_labels:
            if key == "app.subtitle":
                update_info = get_cached_update_info()
                status_text = t("app.subtitle", game_version=get_versions()[1])
                if update_info and not update_info[0]:
                    status_text += f" | {t('update.new_available')} v{update_info[1]}"
                label.configure(text=status_text)
            else:
                label.configure(text=t(key, **fmt))
        for label, key in self.category_frames:
            label.configure(text=t(key))
        for btn, key in self.tool_buttons:
            btn.configure(text=t(key))
        values = [t(f'lang.{code}') for code in ["zh_CN","en_US","ru_RU","fr_FR","es_ES","de_DE","ja_JP","ko_KR"]]
        self.lang_combo.configure(values=values)
        cur = get_language()
        self.lang_combo.set(t(f'lang.{cur}'))
def on_exit():
    try: unlock_self_folder()
    except: pass
    os._exit(0)
if __name__=="__main__":
    hide_console()
    try:
        init_language("zh_CN")
    except Exception:
        pass
    tv,gv=get_versions()
    set_console_title(f"PalworldSaveTools v{tv}")
    clear_console()
    app = MenuGUI()
    try: 
        all_in_one_tool_choice = (1, 0)
        app.run_tool(all_in_one_tool_choice)
    except Exception:
        show_console()
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        raise
    finally:
        on_exit()
    try:
        app.mainloop()
    except Exception:
        show_console()
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        raise
    finally:
        on_exit()