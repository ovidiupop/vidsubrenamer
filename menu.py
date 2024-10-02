# menu.py
import os
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from tkinterweb import HtmlFrame
import ui_functions


def create_menu(root, show_info_callback, _):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    def load_icon(filename):
        try:
            return tk.PhotoImage(file=os.path.join("icons", filename))
        except Exception as e:
            print(f"Error loading icon {filename}: {e}")
            return None

    icons = {
        "exit": load_icon("exit.png"),
        "en": load_icon("en.png"),
        "ro": load_icon("ro.png"),
        "sv": load_icon("sv.png"),
        "info": load_icon("info.png"),
        "about": load_icon("about.png")
    }

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("File"), menu=file_menu, underline=0)
    file_menu.add_command(label=_("Exit"), command=root.quit, accelerator="Ctrl+Q",
                          image=icons["exit"], compound="left")
    root.bind("<Control-q>", lambda e: root.quit())

    language_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("Language"), menu=language_menu, underline=0)
    language_menu.add_command(label="English", command=lambda: (
        root.tk.call('set', 'language', 'en'), root.event_generate("<<ChangeLanguage>>")),
                              image=icons["en"], compound="left")
    language_menu.add_command(label="Română", command=lambda: (
        root.tk.call('set', 'language', 'ro'), root.event_generate("<<ChangeLanguage>>")),
                              image=icons["ro"], compound="left")
    language_menu.add_command(label="Swedish", command=lambda: (
        root.tk.call('set', 'language', 'sv'), root.event_generate("<<ChangeLanguage>>")),
                              image=icons["sv"], compound="left")

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("Help"), menu=help_menu, underline=0)
    help_menu.add_command(label=_("Info"), command=show_info_callback, accelerator="F1",
                          image=icons["info"], compound="left")
    help_menu.add_command(label=_("About"), command=lambda: show_about(root, _), accelerator="F2",
                          image=icons["about"], compound="left")

    root.bind("<F1>", lambda e: show_info_callback())
    root.bind("<F2>", lambda e: show_about(root, _))

    root.menu_icons = icons


def show_info(root, _):
    info_window = tk.Toplevel(root)
    info_window.iconify()
    info_window.title(_("Information"))
    ui_functions.set_icon(info_window)
    html_frame = HtmlFrame(info_window, messages_enabled=False)
    html_frame.pack(expand=True, fill="both")
    language = root.tk.call('set', 'language')
    info_file_path = os.path.join("help", language, "info.html")
    try:
        with open(info_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        html_frame.load_html(html_content)
    except FileNotFoundError:
        print(f"File not found: {info_file_path}")
        html_frame.load_html(_("<p>The info.html file was not found.</p>"))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        html_frame.load_html(_("<p>An error occurred while reading the info.html file: {}</p>").format(str(e)))
    info_window.update_idletasks()
    info_window.minsize(700, 500)
    width = max(700, html_frame.winfo_reqwidth())
    height = max(500, html_frame.winfo_reqheight())
    info_window.geometry(f"{width}x{height}")
    ui_functions.center_window(info_window)
    info_window.deiconify()


def show_about(root, _):
    about_window = tk.Toplevel(root)
    about_window.iconify()
    about_window.title(_("About VidSubRenamer"))
    about_window.minsize(400, 300)
    about_window.geometry("400x300")
    about_window.resizable(False, False)
    ui_functions.set_icon(about_window)
    main_frame = tk.Frame(about_window, bg="#f0f0f0")
    main_frame.pack(fill=tk.BOTH, expand=True)
    title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
    normal_font = tkfont.Font(family="Helvetica", size=12)
    try:
        logo = Image.open("icon/renamer.png")
        logo = logo.resize((100, 100), Image.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(main_frame, image=logo_img, bg="#f0f0f0")
        logo_label.image = logo_img
        logo_label.pack(pady=(20, 10))
    except Exception as e:
        print(f"Error loading logo: {e}")
    tk.Label(main_frame, text="VidSubRenamer", font=title_font, bg="#f0f0f0").pack()
    tk.Label(main_frame, text=_("Version 1.0"), font=normal_font, bg="#f0f0f0").pack()
    tk.Label(main_frame, text="Ovidiu Pop", font=normal_font, bg="#f0f0f0").pack(pady=(10, 0))
    tk.Label(main_frame, text="© 2024", font=normal_font, bg="#f0f0f0").pack()
    close_button = tk.Button(main_frame, text=_("Close"), command=about_window.destroy,
                             bg="#4CAF50", fg="white", font=normal_font)
    close_button.pack(pady=20)
    about_window.update()
    ui_functions.center_window(about_window)
    about_window.deiconify()
    about_window.transient(root)
    about_window.grab_set()
    root.wait_window(about_window)
