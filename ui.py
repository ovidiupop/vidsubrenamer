import tkinter as tk
from tkinter import filedialog, messagebox
import os
import config  # Importă configurările din config.py
import business  # Importă funcțiile de business logic

# Funcție pentru a selecta folderul sursă
def select_folder():
    folder_selected = filedialog.askdirectory(initialdir=config.default_folder)
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)

# Funcție pentru apelarea logica de redenumire
def rename_action():
    folder_path = folder_path_entry.get()
    video_ext = video_ext_var.get()
    subtitle_ext = subtitle_ext_var.get()

    if not folder_path or not video_ext or not subtitle_ext:
        messagebox.showerror("Error", "Toate câmpurile trebuie completate!")
        return

    result_message = business.rename_files(folder_path, video_ext, subtitle_ext)
    messagebox.showinfo("Rezultatul operațiunii", result_message)

# Interfață grafică
def run():
    root = tk.Tk()
    root.title("Renamer Video/Subtitrări")

    # Setăm icoana aplicației folosind un fișier PNG, verificând existența acestuia
    icon_path = "icon/renamer.png"
    if os.path.exists(icon_path):
        try:
            root.iconphoto(False, tk.PhotoImage(file=icon_path))
        except Exception as e:
            print("Eroare la setarea icoanei:", e)
    else:
        print(f"Eroare: Fișierul '{icon_path}' nu există.")

    # Setăm dimensiuni fixe pentru fereastră
    root.geometry("760x200")
    root.resizable(False, False)  # Nu permite redimensionarea ferestrei

    # Stiluri pentru elementele interfeței
    label_font = ("Arial", 12)
    button_font = ("Arial", 10, "bold")
    button_bg = "#4CAF50"
    button_fg = "#FFFFFF"

    # Padding mai mic pentru partea de jos
    global_padding_y = 5

    # Câmp pentru calea folderului
    global folder_path_entry  # Declaram variabila ca globala pentru a putea fi accesata din functii
    folder_path_label = tk.Label(root, text="Calea folderului sursă:", font=label_font)
    folder_path_label.grid(row=0, column=0, padx=10, pady=global_padding_y, sticky="w")

    folder_path_entry = tk.Entry(root, width=40, font=label_font)  # Ajustare lățime
    folder_path_entry.grid(row=0, column=1, padx=10, pady=global_padding_y, sticky="w")

    folder_button = tk.Button(root, text="Selectează folderul", command=select_folder, font=button_font, bg=button_bg, fg=button_fg)
    folder_button.grid(row=0, column=2, padx=10, pady=global_padding_y, sticky="e")

    # Dropdown pentru selectarea extensiei fișierului video
    global video_ext_var  # Facem variabila globală pentru a o accesa în alte funcții
    video_ext_label = tk.Label(root, text="Extensia fișierelor video:", font=label_font)
    video_ext_label.grid(row=1, column=0, padx=10, pady=global_padding_y, sticky="w")

    video_ext_var = tk.StringVar(root)
    video_ext_var.set(config.video_formats[0])  # Setăm prima opțiune din listă ca implicită

    video_ext_menu = tk.OptionMenu(root, video_ext_var, *config.video_formats)
    video_ext_menu.config(font=label_font, width=15)  # Lățime fixă pentru select
    video_ext_menu.grid(row=1, column=1, padx=10, pady=global_padding_y, sticky="w")

    # Dropdown pentru selectarea extensiei subtitrării
    global subtitle_ext_var  # Facem variabila globală pentru a o accesa în alte funcții
    subtitle_ext_label = tk.Label(root, text="Extensia subtitrărilor:", font=label_font)
    subtitle_ext_label.grid(row=2, column=0, padx=10, pady=global_padding_y, sticky="w")

    subtitle_ext_var = tk.StringVar(root)
    subtitle_ext_var.set(config.subtitle_formats[0])  # Setăm prima opțiune din listă ca implicită

    subtitle_ext_menu = tk.OptionMenu(root, subtitle_ext_var, *config.subtitle_formats)
    subtitle_ext_menu.config(font=label_font, width=15)  # Lățime fixă pentru select
    subtitle_ext_menu.grid(row=2, column=1, padx=10, pady=global_padding_y, sticky="w")

    # Buton de submit pentru a redenumi fișierele
    rename_button = tk.Button(root, text="Redenumește fișierele", command=rename_action, font=button_font, bg=button_bg, fg=button_fg)
    rename_button.grid(row=3, column=0, columnspan=3, padx=10, pady=15, sticky="e")  # Butonul este aliniat complet la dreapta

    # Rularea interfeței grafice
    root.mainloop()

# Dacă se lansează direct acest script, rulează interfața
if __name__ == "__main__":
    run()
