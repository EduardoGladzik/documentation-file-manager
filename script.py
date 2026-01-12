import os
from pathlib import Path
import shutil

img_extensions = ['.jpg', '.jpeg', '.png', '.jfif']
DESKTOP_PATH = Path.home() / "Desktop"
CLIENTS_FOLDER = DESKTOP_PATH / "Clientes"
CHECKLIST_PATH = DESKTOP_PATH / "checklist.txt"


def find_client_folder(client_name):
    """
    Searchs for a client folder in the CLIENTS_FOLDER directory.
    """
    categories = ["Avulsos", "Contratados"]
    input_lower = client_name.strip().lower()
    
    for category in categories:
        category_path = CLIENTS_FOLDER / category
        for folder in category_path.iterdir():
            if folder.is_dir() and folder.name.lower() == input_lower:
                return folder
    return None


def is_image_file(filename):
    return any(filename.lower().endswith(ext) for ext in img_extensions)


def move_images_to_photos_folder(rat_folder):
    """
    Moves images from the desktop to the 'Fotos' folder inside the specified RAT folder.
    """
    photos_path = rat_folder / "Fotos"
    os.makedirs(photos_path, exist_ok=True)
    for file in DESKTOP_PATH.iterdir():
        if file.is_file() and is_image_file(file.name):
            try:
                target_path = photos_path / file.name
                shutil.move(str(file), str(target_path))
            except Exception as e:
                print(f"Erro ao mover arquivos: {e}")


def copy_template_checklist(folder_name, rat_path):
    """
    Copies the checklist template to the RAT folder.
    """
    new_file_name = folder_name
    target_path = rat_path / "checklist.txt"
    try:
        shutil.copy(str(CHECKLIST_PATH), str(target_path))
    except Exception as e:
        print(f"Erro ao copiar o checklist: {e}")


def main():
    client_input = input("Insira o nome do cliente: ")
    client_path = find_client_folder(client_input)
    
    if client_path:
        print(f"Cliente encontrado")
        folder_name = f"RAT{input("Insira o número da RAT: ")}"
        rat_path = client_path / folder_name
        move_images_to_photos_folder(rat_path)
        print("Imagens movidas com sucesso para a pasta 'Fotos'.")
        copy_template_checklist(folder_name, rat_path)
        print("Checklist copiado com sucesso.")
    else:
        print(f"Erro: O cliente '{client_input}' não foi encontrado em 'Avulsos' ou 'Contratados'.")
        print("Verifique se o nome está correto ou se a pasta do cliente existe.")        

if __name__ == "__main__":
    main()