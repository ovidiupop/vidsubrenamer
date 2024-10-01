# ui.py
import tkinter as tk
from tkinter import ttk
import os
from controller import Controller
import menu


class RenamerUI:
    def __init__(self, root):
        self.root = root
        self.controller = Controller()
        self.setup_ui()
        self.root.update()  # Forțează actualizarea ferestrei
        self.center_window()  # Centrează fereastra după ce a fost creată

    def setup_ui(self):
        self.root.title(self.controller._("Renamer Video/Subtitles"))
        self.set_icon()
        self.root.geometry("760x300")
        self.root.resizable(False, False)
        self.root.tk.call('set', 'language', self.controller.language)

        # Adăugăm stilul pentru Combobox
        style = ttk.Style()
        style.configure('TCombobox', padding=2)
        style.map('TCombobox', fieldbackground=[('readonly', 'white')])

        menu.create_menu(self.root, lambda: menu.show_info(self.root, self.controller._), self.controller._)
        self.create_widgets()

        self.root.bind("<<ChangeLanguage>>", self.change_language)

    def set_icon(self):
        icon_path = "icon/renamer.png"
        if os.path.exists(icon_path):
            try:
                self.root.iconphoto(False, tk.PhotoImage(file=icon_path))
            except Exception as e:
                print("Error setting icon:", e)
        else:
            print(f"Error: File '{icon_path}' does not exist.")

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.main_frame.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.main_frame.grid_rowconfigure(i, minsize=30)

        # Folder selection
        self.create_folder_selection()

        # Video format selection
        self.create_video_format_selection()

        # Subtitle format selection
        self.create_subtitle_format_selection()

        # Rename direction selection
        self.create_rename_direction_selection()

        # Rename button
        self.create_rename_button()

    def create_folder_selection(self):
        tk.Label(self.main_frame, text=self.controller._("Source folder path:"), font=("Arial", 12)).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        self.folder_path_entry = tk.Entry(self.main_frame, width=40, font=("Arial", 12))
        self.folder_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.folder_path_entry.insert(0, self.controller.default_folder)
        tk.Button(self.main_frame, text=self.controller._("Select folder"), command=self.select_folder,
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="#FFFFFF").grid(row=0, column=2, padx=5, pady=5,
                                                                               sticky="e")

    def create_video_format_selection(self):
        tk.Label(self.main_frame, text=self.controller._("Video files extension:"), font=("Arial", 12)).grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=5,
                                                                                                             pady=5,
                                                                                                             sticky="w")
        self.video_ext_var = tk.StringVar(self.root)
        self.video_ext_var.set(self.controller.default_video_format)
        ttk.Combobox(self.main_frame, textvariable=self.video_ext_var, values=self.controller.video_formats,
                     state="readonly").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.video_ext_var.trace("w", self.update_video_format)

    def create_subtitle_format_selection(self):
        tk.Label(self.main_frame, text=self.controller._("Subtitles extension:"), font=("Arial", 12)).grid(row=2,
                                                                                                           column=0,
                                                                                                           padx=5,
                                                                                                           pady=5,
                                                                                                           sticky="w")
        self.subtitle_ext_var = tk.StringVar(self.root)
        self.subtitle_ext_var.set(self.controller.default_subtitle_format)
        ttk.Combobox(self.main_frame, textvariable=self.subtitle_ext_var, values=self.controller.subtitle_formats,
                     state="readonly").grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.subtitle_ext_var.trace("w", self.update_subtitle_format)

    def create_rename_direction_selection(self):
        tk.Label(self.main_frame, text=self.controller._("Rename direction:"), font=("Arial", 12)).grid(row=3, column=0,
                                                                                                        padx=5, pady=5,
                                                                                                        sticky="w")
        self.rename_direction_var = tk.StringVar(value=self.controller.default_rename_direction)
        tk.Radiobutton(self.main_frame, text=self.controller._("Subtitle → Video"), variable=self.rename_direction_var,
                       value="subtitle_to_video", font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        tk.Radiobutton(self.main_frame, text=self.controller._("Video → Subtitle"), variable=self.rename_direction_var,
                       value="video_to_subtitle", font=("Arial", 12)).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.rename_direction_var.trace("w", self.update_rename_direction)

    def create_rename_button(self):
        tk.Button(self.main_frame, text=self.controller._("Rename files"), command=self.rename_action,
                  font=("Arial", 10, "bold"), bg="#4CAF50", fg="#FFFFFF").grid(row=5, column=0, columnspan=3, padx=5,
                                                                               pady=5, sticky="e")

    def select_folder(self):
        new_folder = self.controller.select_folder(self.folder_path_entry.get())
        self.folder_path_entry.delete(0, tk.END)
        self.folder_path_entry.insert(0, new_folder)

    def update_video_format(self, *args):
        self.controller.update_video_format(self.video_ext_var.get())

    def update_subtitle_format(self, *args):
        self.controller.update_subtitle_format(self.subtitle_ext_var.get())

    def update_rename_direction(self, *args):
        self.controller.update_rename_direction(self.rename_direction_var.get())

    def rename_action(self):
        self.controller.rename_action(
            self.folder_path_entry.get(),
            self.video_ext_var.get(),
            self.subtitle_ext_var.get(),
            self.rename_direction_var.get()
        )

    def change_language(self, event):
        lang = event.widget.tk.call('set', 'language')
        self.controller.change_language(lang)
        self.update_ui_language()

    def update_ui_language(self):
        self.root.title(self.controller._("Renamer Video/Subtitles"))
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()
        menu.create_menu(self.root, lambda: menu.show_info(self.root, self.controller._), self.controller._)
        self.create_widgets()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def run():
    root = tk.Tk()
    app = RenamerUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()