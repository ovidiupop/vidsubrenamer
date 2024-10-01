# ui_components.py
import tkinter as tk
from tkinter import ttk

def create_folder_selection(frame, controller, select_folder_callback):
    label_font = ("Arial", 12)
    button_font = ("Arial", 10, "bold")
    button_bg = "#4CAF50"
    button_fg = "#FFFFFF"
    global_padding = 5

    tk.Label(frame, text=controller._("Source folder path:"), font=label_font).grid(row=0, column=0,
                                                                                    padx=global_padding,
                                                                                    pady=global_padding,
                                                                                    sticky="w")
    folder_path_entry = tk.Entry(frame, width=40, font=label_font)
    folder_path_entry.grid(row=0, column=1, padx=global_padding, pady=global_padding, sticky="ew")
    folder_path_entry.insert(0, controller.default_folder)
    tk.Button(frame, text=controller._("Select folder"), command=select_folder_callback,
              font=button_font, bg=button_bg, fg=button_fg).grid(row=0, column=2, padx=global_padding,
                                                                 pady=global_padding, sticky="e")
    return folder_path_entry

def create_format_selection(frame, controller, video_callback, subtitle_callback):
    label_font = ("Arial", 12)
    global_padding = 5

    tk.Label(frame, text=controller._("Video files extension:"), font=label_font).grid(row=1,
                                                                                       column=0,
                                                                                       padx=global_padding,
                                                                                       pady=global_padding,
                                                                                       sticky="w")
    video_ext_var = tk.StringVar(frame)
    video_ext_var.set(controller.default_video_format)
    video_ext_combo = ttk.Combobox(frame, textvariable=video_ext_var,
                                   values=controller.video_formats, state="readonly", width=10)
    video_ext_combo.grid(row=1, column=1, padx=global_padding, pady=global_padding, sticky="w")
    video_ext_combo.bind("<<ComboboxSelected>>", video_callback)

    tk.Label(frame, text=controller._("Subtitles extension:"), font=label_font).grid(row=2, column=0,
                                                                                     padx=global_padding,
                                                                                     pady=global_padding,
                                                                                     sticky="w")
    subtitle_ext_var = tk.StringVar(frame)
    subtitle_ext_var.set(controller.default_subtitle_format)
    subtitle_ext_combo = ttk.Combobox(frame, textvariable=subtitle_ext_var,
                                      values=controller.subtitle_formats, state="readonly", width=10)
    subtitle_ext_combo.grid(row=2, column=1, padx=global_padding, pady=global_padding, sticky="w")
    subtitle_ext_combo.bind("<<ComboboxSelected>>", subtitle_callback)

    return video_ext_var, subtitle_ext_var

def create_rename_direction(frame, controller, callback):
    label_font = ("Arial", 12)
    global_padding = 5

    tk.Label(frame, text=controller._("Rename direction:"), font=label_font).grid(row=3, column=0,
                                                                                  padx=global_padding,
                                                                                  pady=global_padding,
                                                                                  sticky="w")
    rename_direction_var = tk.StringVar(value=controller.default_rename_direction)
    rename_direction_var.trace("w", callback)
    tk.Radiobutton(frame, text=controller._("Subtitle → Video"), variable=rename_direction_var,
                   value="subtitle_to_video", font=label_font).grid(row=3, column=1, padx=global_padding,
                                                                    pady=global_padding, sticky="w")
    tk.Radiobutton(frame, text=controller._("Video → Subtitle"), variable=rename_direction_var,
                   value="video_to_subtitle", font=label_font).grid(row=4, column=1, padx=global_padding,
                                                                    pady=global_padding, sticky="w")
    return rename_direction_var

def create_rename_button(frame, controller, callback):
    button_font = ("Arial", 10, "bold")
    button_bg = "#4CAF50"
    button_fg = "#FFFFFF"
    global_padding = 5

    tk.Button(frame, text=controller._("Rename files"), command=callback, font=button_font,
              bg=button_bg, fg=button_fg).grid(row=5, column=0, columnspan=3, padx=global_padding,
                                               pady=global_padding, sticky="e")