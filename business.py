# business.py

import os
import re

# Funcție pentru obținerea fișierelor cu extensie specifică
def get_files_with_extension(folder_path, extension):
    return [f for f in os.listdir(folder_path) if f.endswith(f'.{extension}')]

# Funcție pentru extragerea codului SxxEyy din numele fișierului
def extract_episode_code(file_name):
    pattern = r'(S\d{2}E\d{2})'  # Potrivim codul standard SxxEyy
    match = re.search(pattern, file_name, re.IGNORECASE)
    if match:
        return match.group(0)
    return None

# Funcție pentru redenumirea fișierelor video în funcție de subtitrări
def rename_files(folder_path, video_ext, subtitle_ext):
    videos = get_files_with_extension(folder_path, video_ext)
    subtitles = get_files_with_extension(folder_path, subtitle_ext)

    if not videos:
        return f"Nu au fost găsite fișiere video cu extensia {video_ext}."
    if not subtitles:
        return f"Nu au fost găsite subtitrări cu extensia {subtitle_ext}."

    replacement_count = 0

    for video in videos:
        video_episode_code = extract_episode_code(video)
        if not video_episode_code:
            continue

        for subtitle in subtitles:
            subtitle_episode_code = extract_episode_code(subtitle)
            if subtitle_episode_code == video_episode_code:
                new_video_name = f"{os.path.splitext(subtitle)[0]}.{video_ext}"
                old_video_path = os.path.join(folder_path, video)
                new_video_path = os.path.join(folder_path, new_video_name)

                # Redenumește fișierul video
                os.rename(old_video_path, new_video_path)
                replacement_count += 1
                break  # Ieșim din buclă după ce am redenumit fișierul video

    return f"Au fost redenumite {replacement_count} fișiere video."
