# menu.py
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

def create_menu(root, show_info_callback, _):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("File"), menu=file_menu)
    file_menu.add_command(label=_("Exit"), command=root.quit)

    language_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("Language"), menu=language_menu)
    language_menu.add_command(label="English", command=lambda: (root.tk.call('set', 'language', 'en'), root.event_generate("<<ChangeLanguage>>")))
    language_menu.add_command(label="Română", command=lambda: (root.tk.call('set', 'language', 'ro'), root.event_generate("<<ChangeLanguage>>")))
    language_menu.add_command(label="Swedish", command=lambda: (root.tk.call('set', 'language', 'sv'), root.event_generate("<<ChangeLanguage>>")))

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=_("Help"), menu=help_menu)
    help_menu.add_command(label=_("Info"), command=show_info_callback)
    help_menu.add_command(label=_("About"), command=lambda: show_about(_))



def show_info(root, _):
    info_window = tk.Toplevel(root)
    info_window.title(_("Information"))
    info_window.geometry("700x500")
    info_window.update_idletasks()
    width = info_window.winfo_width()
    height = info_window.winfo_height()
    x = (info_window.winfo_screenwidth() // 2) - (width // 2)
    y = (info_window.winfo_screenheight() // 2) - (height // 2)
    info_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    info_text = scrolledtext.ScrolledText(info_window, wrap=tk.WORD, width=60, height=15)
    info_text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    language = root.tk.call('set', 'language')
    info_file_path = os.path.join("help", language, "info.txt")

    try:
        with open(info_file_path, "r", encoding="utf-8") as file:
            info_content = file.read()
        info_text.insert(tk.END, info_content)
    except FileNotFoundError:
        info_text.insert(tk.END, _("The info.txt file was not found."))
    except Exception as e:
        info_text.insert(tk.END, _("An error occurred while reading the info.txt file: {}").format(str(e)))

    info_text.config(state=tk.DISABLED)  # Make the text read-only

def show_about(_):
    about_message = _("Renamer Video/Subtitles\n\nVersion 1.0\n\nCreated by [Your Name]\n\n© 2024 All rights reserved")
    messagebox.showinfo(_("About"), about_message)