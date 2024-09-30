import tkinter as tk
from tkinter import messagebox, scrolledtext


def create_menu(root, show_info_callback):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Info", command=show_info_callback)
    help_menu.add_command(label="About", command=show_about)


def show_info(root):
    info_window = tk.Toplevel(root)
    info_window.title("Informații")
    info_window.geometry("500x300")

    info_text = scrolledtext.ScrolledText(info_window, wrap=tk.WORD, width=60, height=15)
    info_text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    try:
        with open("info.txt", "r", encoding="utf-8") as file:
            info_content = file.read()
        info_text.insert(tk.END, info_content)
    except FileNotFoundError:
        info_text.insert(tk.END, "Fișierul info.txt nu a fost găsit.")
    except Exception as e:
        info_text.insert(tk.END, f"A apărut o eroare la citirea fișierului info.txt: {str(e)}")

    info_text.config(state=tk.DISABLED)  # Face textul doar pentru citire


def show_about():
    about_message = "Renamer Video/Subtitrări\n\nVersiune 1.0\n\nCreat de [Numele Tău]\n\n© 2024 Toate drepturile rezervate"
    messagebox.showinfo("Despre", about_message)