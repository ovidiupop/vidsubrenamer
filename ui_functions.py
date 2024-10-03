# ui_functions.py
import os
import tkinter as tk

import menu


def set_icon(root):
    icon_path = menu.resource_path(os.path.join("icon", "renamer.png"))
    print(f"Attempting to set icon from: {icon_path}")
    if os.path.exists(icon_path):
        try:
            icon = tk.PhotoImage(file=icon_path)
            root.iconphoto(False, icon)
            print("Icon set successfully")
        except Exception as e:
            print(f"Error setting icon: {e}")
            print(f"Icon path: {icon_path}")
            print(f"File exists: {os.path.exists(icon_path)}")
            print(f"File size: {os.path.getsize(icon_path)}")
    else:
        print(f"Error: File '{icon_path}' does not exist.")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Contents of icon directory: {os.listdir(menu.resource_path('icon'))}")


def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


# def center_window(root):
#     # root.update_idletasks()
#     width = root.winfo_width()
#     height = root.winfo_height()
#
#     if os.name == 'nt':  # Windows
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight() - 60
#         x = (screen_width // 2) - (width // 2)
#         y = (screen_height // 2) - (height // 2)
#         root.geometry(f'{width}x{height}+{x}+{y}')
#
#         try:
#             from ctypes import windll
#             windll.shcore.SetProcessDpiAwareness(1)
#         except:
#             pass
#     else:  # Linux
#         x = (root.winfo_screenwidth() // 2) - (width // 2)
#         y = (root.winfo_screenheight() // 2) - (height // 2)
#         root.geometry(f'{width}x{height}+{x}+{y}')
#     root.update()

def center_main_window(root, width, height):
    # root.update_idletasks()
    # width = root.winfo_width()
    # height = root.winfo_height()

    if os.name == 'nt':  # Windows
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() - 60
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')

        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
    else:  # Linux
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        root.update_idletasks()
    root.update()


def select_folder(controller, folder_path_entry):
    new_folder = controller.select_folder(folder_path_entry.get())
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, new_folder)


def update_video_format(controller, video_ext_var):
    controller.update_video_format(video_ext_var.get())


def update_subtitle_format(controller, subtitle_ext_var):
    controller.update_subtitle_format(subtitle_ext_var.get())


def update_rename_direction(controller, rename_direction_var):
    controller.update_rename_direction(rename_direction_var.get())


def rename_action(controller, folder_path_entry, video_ext_var, subtitle_ext_var, rename_direction_var):
    controller.rename_action(
        folder_path_entry.get(),
        video_ext_var.get(),
        subtitle_ext_var.get(),
        rename_direction_var.get()
    )


def change_language(controller, root, event, main_frame, create_widgets_callback):
    lang = event.widget.tk.call('set', 'language')
    controller.change_language(lang)

    # Logica fostei funcții update_ui_language
    root.title(controller._("VidSubRenamer"))
    if main_frame:
        main_frame.destroy()
    menu.create_menu(root, lambda: menu.show_info(root, controller._), controller._)
    create_widgets_callback()
