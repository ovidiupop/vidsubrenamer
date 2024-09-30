import tkinter as tk
from tkinter import filedialog, messagebox
import os
import config
import business
import menu


def select_folder():
    folder_selected = filedialog.askdirectory(initialdir=folder_path_entry.get())
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)
        config.update_config(new_folder=folder_selected)


def update_video_format(*args):
    selected_format = video_ext_var.get()
    config.update_config(new_video_format=selected_format)


def update_subtitle_format(*args):
    selected_format = subtitle_ext_var.get()
    config.update_config(new_subtitle_format=selected_format)


def update_rename_direction(*args):
    selected_direction = rename_direction_var.get()
    config.update_config(new_rename_direction=selected_direction)


def rename_action():
    folder_path = folder_path_entry.get()
    video_ext = video_ext_var.get()
    subtitle_ext = subtitle_ext_var.get()
    rename_direction = rename_direction_var.get()

    if not folder_path or not video_ext or not subtitle_ext:
        messagebox.showerror("Error", "Toate câmpurile trebuie completate!")
        return

    if rename_direction == "video_to_subtitle":
        source_ext = video_ext
        target_ext = subtitle_ext
    else:
        source_ext = subtitle_ext
        target_ext = video_ext

    result_message = business.rename_files(folder_path, source_ext, target_ext)
    messagebox.showinfo("Rezultatul operațiunii", result_message)


def run():
    global root, folder_path_entry, video_ext_var, subtitle_ext_var, rename_direction_var
    root = tk.Tk()
    root.title("Renamer Video/Subtitrări")

    icon_path = "icon/renamer.png"
    if os.path.exists(icon_path):
        try:
            root.iconphoto(False, tk.PhotoImage(file=icon_path))
        except Exception as e:
            print("Eroare la setarea icoanei:", e)
    else:
        print(f"Eroare: Fișierul '{icon_path}' nu există.")

    root.geometry("760x250")
    root.resizable(False, False)

    menu.create_menu(root, lambda: menu.show_info(root))

    label_font = ("Arial", 12)
    button_font = ("Arial", 10, "bold")
    button_bg = "#4CAF50"
    button_fg = "#FFFFFF"

    global_padding_y = 5

    folder_path_label = tk.Label(root, text="Calea folderului sursă:", font=label_font)
    folder_path_label.grid(row=0, column=0, padx=10, pady=global_padding_y, sticky="w")

    folder_path_entry = tk.Entry(root, width=40, font=label_font)
    folder_path_entry.grid(row=0, column=1, padx=10, pady=global_padding_y, sticky="w")
    folder_path_entry.insert(0, config.default_folder)

    folder_button = tk.Button(root, text="Selectează folderul", command=select_folder, font=button_font, bg=button_bg,
                              fg=button_fg)
    folder_button.grid(row=0, column=2, padx=10, pady=global_padding_y, sticky="e")

    video_ext_label = tk.Label(root, text="Extensia fișierelor video:", font=label_font)
    video_ext_label.grid(row=1, column=0, padx=10, pady=global_padding_y, sticky="w")

    video_ext_var = tk.StringVar(root)
    video_ext_var.set(config.default_video_format)
    video_ext_var.trace("w", update_video_format)

    video_ext_menu = tk.OptionMenu(root, video_ext_var, *config.video_formats)
    video_ext_menu.config(font=label_font, width=15)
    video_ext_menu.grid(row=1, column=1, padx=10, pady=global_padding_y, sticky="w")

    subtitle_ext_label = tk.Label(root, text="Extensia subtitrărilor:", font=label_font)
    subtitle_ext_label.grid(row=2, column=0, padx=10, pady=global_padding_y, sticky="w")

    subtitle_ext_var = tk.StringVar(root)
    subtitle_ext_var.set(config.default_subtitle_format)
    subtitle_ext_var.trace("w", update_subtitle_format)

    subtitle_ext_menu = tk.OptionMenu(root, subtitle_ext_var, *config.subtitle_formats)
    subtitle_ext_menu.config(font=label_font, width=15)
    subtitle_ext_menu.grid(row=2, column=1, padx=10, pady=global_padding_y, sticky="w")

    rename_direction_var = tk.StringVar(value=config.default_rename_direction)
    rename_direction_var.trace("w", update_rename_direction)

    rename_direction_label = tk.Label(root, text="Direcția de redenumire:", font=label_font)
    rename_direction_label.grid(row=3, column=0, padx=10, pady=global_padding_y, sticky="w")

    subtitle_to_video_radio = tk.Radiobutton(root, text="Subtitrare → Video", variable=rename_direction_var,
                                             value="subtitle_to_video", font=label_font)
    subtitle_to_video_radio.grid(row=3, column=1, padx=10, pady=global_padding_y, sticky="w")

    video_to_subtitle_radio = tk.Radiobutton(root, text="Video → Subtitrare", variable=rename_direction_var,
                                             value="video_to_subtitle", font=label_font)
    video_to_subtitle_radio.grid(row=4, column=1, padx=10, pady=global_padding_y, sticky="w")

    rename_button = tk.Button(root, text="Redenumește fișierele", command=rename_action, font=button_font, bg=button_bg,
                              fg=button_fg)
    rename_button.grid(row=5, column=0, columnspan=3, padx=10, pady=15, sticky="e")

    root.mainloop()


if __name__ == "__main__":
    run()