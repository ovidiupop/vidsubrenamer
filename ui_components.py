# ui_components.py
import tkinter as tk
from tkinter import ttk


def create_folder_selection(frame, controller, select_folder_callback):
    tk.Label(frame, text=controller._("Source folder path:"), font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5,
                                                                                       sticky="w")
    folder_path_entry = tk.Entry(frame, width=40, font=("Arial", 12))
    folder_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    folder_path_entry.insert(0, controller.default_folder)
    tk.Button(frame, text=controller._("Select folder"), command=select_folder_callback,
              font=("Arial", 10, "bold"), bg="#4CAF50", fg="#FFFFFF").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    return folder_path_entry


def create_format_selection(frame, controller, label_text, row, callback):
    tk.Label(frame, text=controller._(label_text), font=("Arial", 12)).grid(row=row, column=0, padx=5, pady=5,
                                                                            sticky="w")
    var = tk.StringVar(frame)
    var.set(controller.default_video_format if "Video" in label_text else controller.default_subtitle_format)
    ttk.Combobox(frame, textvariable=var,
                 values=controller.video_formats if "Video" in label_text else controller.subtitle_formats,
                 state="readonly").grid(row=row, column=1, padx=5, pady=5, sticky="w")
    var.trace("w", callback)
    return var


def create_rename_direction_selection(frame, controller, callback):
    tk.Label(frame, text=controller._("Rename direction:"), font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5,
                                                                                     sticky="w")
    rename_direction_var = tk.StringVar(value=controller.default_rename_direction)
    tk.Radiobutton(frame, text=controller._("Subtitle → Video"), variable=rename_direction_var,
                   value="subtitle_to_video", font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5, sticky="w")
    tk.Radiobutton(frame, text=controller._("Video → Subtitle"), variable=rename_direction_var,
                   value="video_to_subtitle", font=("Arial", 12)).grid(row=4, column=1, padx=5, pady=5, sticky="w")
    rename_direction_var.trace("w", callback)
    return rename_direction_var


def create_rename_button(frame, controller, callback):
    tk.Button(frame, text=controller._("Rename files"), command=callback,
              font=("Arial", 10, "bold"), bg="#4CAF50", fg="#FFFFFF").grid(row=5, column=0, columnspan=3, padx=5,
                                                                           pady=5, sticky="e")
