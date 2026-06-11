from pathlib import Path


def get_extension(file_path: str) -> str:
    return Path(file_path).suffix.lower()