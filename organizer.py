from pathlib import Path

CATEGORIES = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".tiff": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".heic": "Images",
    
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".pptx": "Documents",
    ".ppt": "Documents",
    ".csv": "Documents",
    ".md": "Documents",
    
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",
    
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".iso": "Archives",
    
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio"
}

str_path = input("Enter filepath: ")
path = Path(str_path)

files = [x for x in path.iterdir() if x.is_file()]

for f in files:
    for ex, c in CATEGORIES.items():
        if f.suffix == ex:
            destination = Path(f"{str_path}/{c}")
            destination.mkdir(parents=True, exist_ok=True)

            target_path = destination / f.name
            f.rename(target_path)

for p in path.iterdir():
    print(p.name)