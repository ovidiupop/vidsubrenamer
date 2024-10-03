# ui.py
import os
import tkinter as tk
from tkinter import ttk
from controller import Controller
import menu
import ui_components
import ui_functions


class RenamerUI:
    def __init__(self, root):
        self.root = root
        self.controller = Controller()
        self.setup_ui()

    def setup_ui(self):
        self.root.title(self.controller._("VidSubRenamer"))
        self.root.tk.call('set', 'language', self.controller.language)
        style = ttk.Style()
        style.configure('TCombobox', padding=2)
        style.map('TCombobox', fieldbackground=[('readonly', 'white')])
        self.create_widgets()
        # ui_functions.center_window(self.root)
        ui_functions.set_icon(self.root)
        self.root.resizable(False, False)
        menu.create_menu(self.root, lambda: menu.show_info(self.root, self.controller._), self.controller._)

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.main_frame.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.main_frame.grid_rowconfigure(i, minsize=30)

        self.folder_path_entry = ui_components.create_folder_selection(self.main_frame, self.controller,
                                                                       lambda: ui_functions.select_folder(
                                                                           self.controller, self.folder_path_entry))
        self.video_ext_var = ui_components.create_format_selection(self.main_frame, self.controller,
                                                                   "Video files extension:", 1,
                                                                   lambda *args: ui_functions.update_video_format(
                                                                       self.controller, self.video_ext_var))
        self.subtitle_ext_var = ui_components.create_format_selection(self.main_frame, self.controller,
                                                                      "Subtitles extension:", 2,
                                                                      lambda *args: ui_functions.update_subtitle_format(
                                                                          self.controller, self.subtitle_ext_var))
        self.rename_direction_var = ui_components.create_rename_direction_selection(self.main_frame, self.controller,
                                                                                    lambda
                                                                                        *args: ui_functions.update_rename_direction(
                                                                                        self.controller,
                                                                                        self.rename_direction_var))
        ui_components.create_rename_button(self.main_frame, self.controller,
                                           lambda: ui_functions.rename_action(self.controller, self.folder_path_entry,
                                                                              self.video_ext_var, self.subtitle_ext_var,
                                                                              self.rename_direction_var))
        self.root.bind("<<ChangeLanguage>>",
                       lambda event: ui_functions.change_language(self.controller, self.root, event, self.main_frame,
                                                                  self.create_widgets))


def run():
    root = tk.Tk()
    RenamerUI(root)

    if os.name != 'nt':
        root.iconify()

    ui_functions.center_main_window(root, 660, 260)

    if os.name != 'nt':
        root.deiconify()

    root.mainloop()


if __name__ == "__main__":
    run()
