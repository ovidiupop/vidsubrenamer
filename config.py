import json
import os

config_path = os.path.expanduser("~/.config/renamer/config.json")

# Configurație implicită
default_config = {
    "default_folder": "",
    "video_formats": ["mp4", "mkv", "avi", "mov", "wmv"],
    "subtitle_formats": ["srt", "sub", "ass", "ssa"],
    "default_video_format": "mp4",
    "default_subtitle_format": "srt",
    "default_rename_direction": "subtitle_to_video"  # Adăugat
}


def load_config():
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        save_config(default_config)
        return default_config

    with open(config_path, 'r') as f:
        return json.load(f)


def save_config(config_data):
    with open(config_path, 'w') as f:
        json.dump(config_data, f, indent=4)


config = load_config()


def update_config(new_folder=None, new_video_format=None, new_subtitle_format=None, new_rename_direction=None):
    global config
    if new_folder:
        config["default_folder"] = new_folder
    if new_video_format:
        config["default_video_format"] = new_video_format
    if new_subtitle_format:
        config["default_subtitle_format"] = new_subtitle_format
    if new_rename_direction:
        config["default_rename_direction"] = new_rename_direction
    save_config(config)


# Expunem variabilele necesare
video_formats = config["video_formats"]
subtitle_formats = config["subtitle_formats"]
default_folder = config["default_folder"]
default_video_format = config["default_video_format"]
default_subtitle_format = config["default_subtitle_format"]
default_rename_direction = config["default_rename_direction"]  # Adăugat