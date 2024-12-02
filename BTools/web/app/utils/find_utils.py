import os

def search_files_by_name(directory, keyword):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword in file:
                matched_files.append(os.path.join(root, file))
    return matched_files

def search_files_by_content(directory, keyword):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if keyword in f.read():
                        matched_files.append(file_path)
            except (UnicodeDecodeError, FileNotFoundError, PermissionError):
                continue
    return matched_files