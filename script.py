import os
from pathlib import Path

img_extensions = ['.jpg', '.jpeg', '.png', '.jfif']
BASE_PATH = Path.home() / "Desktop"


def create_standard_folder_structure(folder_name):
    full_path = BASE_PATH / folder_name / "Fotos"
    os.makedirs(full_path, exist_ok=True)


def is_image_file(filename):
    return any(filename.lower().endswith(ext) for ext in img_extensions)


folder_name = f"RAT{input("Insira o número da RAT: ")}"
create_standard_folder_structure(folder_name=folder_name)

for file in BASE_PATH.iterdir():
    if is_image_file(file.name):
        target_folder = BASE_PATH / folder_name / "Fotos"
        target_path = target_folder / file.name
        file.rename(target_path)
        print(f"Moved {file.name} to {target_path}")