# services/file_service.py

from pathlib import Path

from utils.logger import logger


def read_file(file_path):
    """
    Reads the content of a file and returns it along with the file name.
    """
    logger.info(f"Reading file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    file_name = Path(file_path).name
    return content, file_name