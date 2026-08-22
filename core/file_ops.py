from pathlib import Path


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    file_name = Path(file_path).name
    return content, file_name