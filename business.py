import os
import re


def get_files_with_extension(folder_path, extension):
    return [f for f in os.listdir(folder_path) if f.endswith(f'{extension}')]


def extract_episode_code(file_name):
    pattern = r'(S\d{2}E\d{2})'
    match = re.search(pattern, file_name, re.IGNORECASE)
    if match:
        return match.group(0)
    return None


def rename_files(folder_path, source_ext, target_ext):
    source_files = get_files_with_extension(folder_path, source_ext)
    target_files = get_files_with_extension(folder_path, target_ext)

    if not source_files:
        return f"Nu au fost găsite fișiere sursă cu extensia {source_ext}."
    if not target_files:
        return f"Nu au fost găsite fișiere țintă cu extensia {target_ext}."

    replacement_count = 0

    for source in source_files:
        source_episode_code = extract_episode_code(source)
        if not source_episode_code:
            continue

        for target in target_files:
            target_episode_code = extract_episode_code(target)
            if target_episode_code == source_episode_code:
                new_target_name = f"{os.path.splitext(source)[0]}.{target_ext}"
                old_target_path = os.path.join(folder_path, target)
                new_target_path = os.path.join(folder_path, new_target_name)

                os.rename(old_target_path, new_target_path)
                replacement_count += 1
                break

    return f"Au fost redenumite {replacement_count} fișiere țintă."
