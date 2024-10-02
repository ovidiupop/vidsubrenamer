# config.py
import json
import os

config_path = os.path.expanduser("~/.config/VidSubRenamer/config.json")

default_config = {
    "default_folder": "",
    "video_formats": ["mp4", "mkv", "avi", "mov", "wmv"],
    "subtitle_formats": ["srt", "sub", "ass", "ssa"],
    "default_video_format": "mp4",
    "default_subtitle_format": "srt",
    "default_rename_direction": "subtitle_to_video",
    "language": "en"
}


def load_config():
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        save_config(default_config)
        return default_config

    with open(config_path, 'r') as f:
        loaded_config = json.load(f)
        for key, value in default_config.items():
            if key not in loaded_config:
                loaded_config[key] = value
        return loaded_config


def save_config(config_data):
    with open(config_path, 'w') as f:
        json.dump(config_data, f, indent=4)


config = load_config()

language = config["language"]
video_formats = config["video_formats"]
subtitle_formats = config["subtitle_formats"]
default_folder = config["default_folder"]
default_video_format = config["default_video_format"]
default_subtitle_format = config["default_subtitle_format"]
default_rename_direction = config["default_rename_direction"]


def update_config(new_folder=None, new_video_format=None, new_subtitle_format=None, new_rename_direction=None,
                  new_language=None):
    global config
    if new_folder:
        config["default_folder"] = new_folder
    if new_video_format:
        config["default_video_format"] = new_video_format
    if new_subtitle_format:
        config["default_subtitle_format"] = new_subtitle_format
    if new_rename_direction:
        config["default_rename_direction"] = new_rename_direction
    if new_language:
        config["language"] = new_language
    save_config(config)
