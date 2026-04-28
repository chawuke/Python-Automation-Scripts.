import os
import shutil

# Script simple para organizar carpetas por tipo de archivo
def organize_folder(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        ext = file.split('.')[-1].lower()
        folder_name = os.path.join(path, ext.upper() + "_Files")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        shutil.move(os.path.join(path, file), os.path.join(folder_name, file))
    print("¡Carpeta organizada!")

# Úsalo en el directorio actual
if __name__ == "__main__":
    organize_folder(".")
