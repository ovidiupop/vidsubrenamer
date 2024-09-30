# ui.py
import tkinter as tk
import os
from controller import Controller
import menu

class RenamerUI:
    def __init__(self, root):
        self.root = root
        self.controller = Controller()
        self.setup_ui()

    def setup_ui(self):
        self.root.title(self.controller._("Renamer Video/Subtitles"))
        self.set_icon()
        self.root.geometry("760x300")
        self.root.resizable(False, False)
        self.root.tk.call('set', 'language', self.controller.language)

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

        label_font = ("Arial", 12)
        button_font = ("Arial", 10, "bold")
        button_bg = "#4CAF50"
        button_fg = "#FFFFFF"
        global_padding = 5

        # Configurare grid
        self.main_frame.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.main_frame.grid_rowconfigure(i, minsize=30)

        # Folder selection
        tk.Label(self.main_frame, text=self.controller._("Source folder path:"), font=label_font).grid(row=0, column=0,
                                                                                                       padx=global_padding,
                                                                                                       pady=global_padding,
                                                                                                       sticky="w")
        self.folder_path_entry = tk.Entry(self.main_frame, width=40, font=label_font)
        self.folder_path_entry.grid(row=0, column=1, padx=global_padding, pady=global_padding, sticky="ew")
        self.folder_path_entry.insert(0, self.controller.default_folder)
        tk.Button(self.main_frame, text=self.controller._("Select folder"), command=self.select_folder,
                  font=button_font, bg=button_bg, fg=button_fg).grid(row=0, column=2, padx=global_padding,
                                                                     pady=global_padding, sticky="e")

        # Video format selection
        tk.Label(self.main_frame, text=self.controller._("Video files extension:"), font=label_font).grid(row=1,
                                                                                                          column=0,
                                                                                                          padx=global_padding,
                                                                                                          pady=global_padding,
                                                                                                          sticky="w")
        self.video_ext_var = tk.StringVar(self.root)
        self.video_ext_var.set(self.controller.default_video_format)
        self.video_ext_var.trace("w", self.update_video_format)
        tk.OptionMenu(self.main_frame, self.video_ext_var, *self.controller.video_formats).grid(row=1, column=1,
                                                                                                padx=global_padding,
                                                                                                pady=global_padding,
                                                                                                sticky="w")

        # Subtitle format selection
        tk.Label(self.main_frame, text=self.controller._("Subtitles extension:"), font=label_font).grid(row=2, column=0,
                                                                                                        padx=global_padding,
                                                                                                        pady=global_padding,
                                                                                                        sticky="w")
        self.subtitle_ext_var = tk.StringVar(self.root)
        self.subtitle_ext_var.set(self.controller.default_subtitle_format)
        self.subtitle_ext_var.trace("w", self.update_subtitle_format)
        tk.OptionMenu(self.main_frame, self.subtitle_ext_var, *self.controller.subtitle_formats).grid(row=2, column=1,
                                                                                                      padx=global_padding,
                                                                                                      pady=global_padding,
                                                                                                      sticky="w")

        # Rename direction selection
        tk.Label(self.main_frame, text=self.controller._("Rename direction:"), font=label_font).grid(row=3, column=0,
                                                                                                     padx=global_padding,
                                                                                                     pady=global_padding,
                                                                                                     sticky="w")
        self.rename_direction_var = tk.StringVar(value=self.controller.default_rename_direction)
        self.rename_direction_var.trace("w", self.update_rename_direction)
        tk.Radiobutton(self.main_frame, text=self.controller._("Subtitle → Video"), variable=self.rename_direction_var,
                       value="subtitle_to_video", font=label_font).grid(row=3, column=1, padx=global_padding,
                                                                        pady=global_padding, sticky="w")
        tk.Radiobutton(self.main_frame, text=self.controller._("Video → Subtitle"), variable=self.rename_direction_var,
                       value="video_to_subtitle", font=label_font).grid(row=4, column=1, padx=global_padding,
                                                                        pady=global_padding, sticky="w")

        # Rename button
        tk.Button(self.main_frame, text=self.controller._("Rename files"), command=self.rename_action, font=button_font,
                  bg=button_bg, fg=button_fg).grid(row=5, column=0, columnspan=3, padx=global_padding,
                                                   pady=global_padding, sticky="e")
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
        self.resize_window()

    def resize_window(self):
        self.root.update_idletasks()  # Actualizează toate sarcinile în așteptare
        self.root.geometry('')  # Resetează geometria ferestrei
        self.root.geometry(f"+{self.root.winfo_x()}+{self.root.winfo_y()}")  # Păstrează poziția ferestrei


def run():
    root = tk.Tk()
    app = RenamerUI(root)
    root.mainloop()

if __name__ == "__main__":
    run()