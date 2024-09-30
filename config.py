import json
import os
import shutil

# Calea către fișierul de configurare
config_path = os.path.expanduser("~/.config/renamer/config.json")

default_config_path = os.path.join(os.path.dirname(__file__), 'config.json')

# Verificăm dacă directorul există, dacă nu, îl creăm
os.makedirs(os.path.dirname(config_path), exist_ok=True)

# Copiem fișierul de configurare dacă nu există
if not os.path.exists(config_path):
    shutil.copy(default_config_path, config_path)

# Funcție pentru a încărca configurația
def load_config():
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as f:
        return json.load(f)

# Încarcă configurația
config = load_config()

# Variabilele pe care le folosești în aplicație
video_formats = config.get("video_formats", [])
subtitle_formats = config.get("subtitle_formats", [])
default_folder = config.get("default_folder", "")
