# Renamer Application

## Overview
The **Renamer Application** is a Python-based utility designed to simplify the renaming of video files and their corresponding subtitle files. The application provides a user-friendly graphical interface (using Tkinter) that allows users to select a folder, choose specific file extensions for videos and subtitles, and automate the renaming process to ensure file names match.

The application reads configuration options from a JSON file located in the user’s config directory (`~/.config/renamer/config.json`), allowing flexibility and customization for various formats.

## Features
- **Batch Renaming**: Automatically rename video files and matching subtitles in bulk.
- **User-friendly Interface**: Simple and intuitive graphical interface built with Tkinter.
- **Custom File Formats**: Supports multiple video and subtitle file formats, configurable through `config.json`.
- **Default Folder Selection**: Users can set a default folder for quick access.
- **Icon Support**: Application window displays a custom icon (PNG or ICO format).
- **Cross-platform**: Works on Linux and potentially other platforms where Python and Tkinter are supported.

## Requirements
- **Python 3**
- **Tkinter** (for the GUI)
- Required Python packages can be installed from `requirements.txt`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/renamer.git
   cd renamer
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   ```bash
   pip install -r requirements.txt 

3. Run the application:
	``` bash
	python renamer.py

## Usage

Open the Application

**Select Folder**: Use the Select Folder button to choose the directory containing your video and subtitle files.

**Choose Formats**: Pick the file extensions for video and subtitle files from the dropdown menus.

**Rename Files**: Click the Rename Files button to automatically rename the files so they match.


## Configuration File
* The application uses a configuration file stored at ~/.config/renamer/config.json.	
	```
	{
	    "video_formats": [".mp4", ".mkv", ".avi"],
	    "subtitle_formats": [".srt", ".sub"],
	    "default_folder": "/home/user/Videos"
	}
	```

## Building an Executable
You can build a standalone executable using PyInstaller:
```
pyinstaller --onefile --windowed --add-data "config.json:." --add-data "icon/renamer.png:icon" --icon=icon/renamer.ico renamer.py
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
