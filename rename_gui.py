import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Definirea tipurilor de fișiere video și subtitrări
video_formats = ['mkv', 'mp4', 'avi']
subtitle_formats = ['srt', 'sub']

# Funcție pentru obținerea fișierelor cu extensie specifică
def get_files_with_extension(folder_path, extension):
    return [f for f in os.listdir(folder_path) if f.endswith(f'.{extension}')]

# Funcție pentru extragerea codului SxxEyy din numele fișierului
def extract_episode_code(file_name):
    pattern = r'(S\d{2}E\d{2})'  # Potrivim codul standard SxxEyy
    match = re.search(pattern, file_name, re.IGNORECASE)
    if match:
        return match.group(0)
    return None

# Funcție pentru redenumirea fișierelor video
def rename_files():
    folder_path = folder_path_entry.get()
    video_ext = video_ext_var.get()
    subtitle_ext = subtitle_ext_var.get()

    if not folder_path or not video_ext or not subtitle_ext:
        messagebox.showerror("Error", "Toate câmpurile trebuie completate!")
        return

    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Calea folderului este invalidă!")
        return

    videos = get_files_with_extension(folder_path, video_ext)
    subtitles = get_files_with_extension(folder_path, subtitle_ext)

    if not videos:
        messagebox.showerror("Error", f"Nu au fost găsite fișiere video cu extensia {video_ext}")
        return
    if not subtitles:
        messagebox.showerror("Error", f"Nu au fost găsite subtitrări cu extensia {subtitle_ext}")
        return

    replacement_count = 0

    for video in videos:
        video_episode_code = extract_episode_code(video)
        if not video_episode_code:
            continue

        for subtitle in subtitles:
            subtitle_episode_code = extract_episode_code(subtitle)
            if subtitle_episode_code == video_episode_code:
                new_video_name = f"{os.path.splitext(subtitle)[0]}.{video_ext}"
                old_video_path = os.path.join(folder_path, video)
                new_video_path = os.path.join(folder_path, new_video_name)

                # Redenumește fișierul video
                os.rename(old_video_path, new_video_path)
                replacement_count += 1
                break  # Ieșim din buclă după ce am redenumit fișierul video

    messagebox.showinfo("Succes", f"Au fost redenumite {replacement_count} fișiere video!")

# Funcție pentru a selecta folderul sursă
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)

# Interfață grafică
root = tk.Tk()
root.title("Renamer Video/Subtitrări")

# Câmp pentru calea folderului
folder_path_label = tk.Label(root, text="Calea folderului sursă:")
folder_path_label.grid(row=0, column=0, padx=10, pady=10)

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

folder_button = tk.Button(root, text="Selectează folderul", command=select_folder)
folder_button.grid(row=0, column=2, padx=10, pady=10)

# Dropdown pentru selectarea extensiei fișierului video
video_ext_label = tk.Label(root, text="Extensia fișierelor video:")
video_ext_label.grid(row=1, column=0, padx=10, pady=10)

video_ext_var = tk.StringVar(root)
video_ext_var.set(video_formats[0])  # Setăm prima opțiune din listă ca implicită

video_ext_menu = tk.OptionMenu(root, video_ext_var, *video_formats)
video_ext_menu.grid(row=1, column=1, padx=10, pady=10)

# Dropdown pentru selectarea extensiei subtitrării
subtitle_ext_label = tk.Label(root, text="Extensia subtitrărilor:")
subtitle_ext_label.grid(row=2, column=0, padx=10, pady=10)

subtitle_ext_var = tk.StringVar(root)
subtitle_ext_var.set(subtitle_formats[0])  # Setăm prima opțiune din listă ca implicită

subtitle_ext_menu = tk.OptionMenu(root, subtitle_ext_var, *subtitle_formats)
subtitle_ext_menu.grid(row=2, column=1, padx=10, pady=10)

# Buton de submit pentru a redenumi fișierele
rename_button = tk.Button(root, text="Redenumește fișierele", command=rename_files)
rename_button.grid(row=3, columnspan=3, padx=10, pady=20)

# Rularea interfeței grafice
root.mainloop()
