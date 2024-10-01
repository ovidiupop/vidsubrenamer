# controller.py
import config
import business
from tkinter import messagebox, filedialog
from localization import setup_localization

class Controller:
    def __init__(self):
        self.load_config()
        self.language = config.language
        self._ = setup_localization(self.language)

    def load_config(self):
        self.default_folder = config.default_folder
        self.default_video_format = config.default_video_format
        self.default_subtitle_format = config.default_subtitle_format
        self.default_rename_direction = config.default_rename_direction
        self.video_formats = config.video_formats
        self.subtitle_formats = config.subtitle_formats

    def select_folder(self, current_folder):
        folder_selected = filedialog.askdirectory(initialdir=current_folder)
        if folder_selected:
            config.update_config(new_folder=folder_selected)
            return folder_selected
        return current_folder

    def update_video_format(self, selected_format):
        config.update_config(new_video_format=selected_format)

    def update_subtitle_format(self, selected_format):
        config.update_config(new_subtitle_format=selected_format)

    def update_rename_direction(self, selected_direction):
        config.update_config(new_rename_direction=selected_direction)

    def rename_action(self, folder_path, video_ext, subtitle_ext, rename_direction):
        if not folder_path or not video_ext or not subtitle_ext:
            messagebox.showerror(self._("Error"), self._("All fields must be completed!"))
            return

        if rename_direction == "video_to_subtitle":
            source_ext = video_ext
            target_ext = subtitle_ext
        else:
            source_ext = subtitle_ext
            target_ext = video_ext

        result_message = business.rename_files(folder_path, source_ext, target_ext)
        messagebox.showinfo(self._("Operation Result"), result_message)

    def change_language(self, new_language):
        config.update_config(new_language=new_language)
        self._ = setup_localization(new_language)