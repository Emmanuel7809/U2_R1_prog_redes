#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
import os
def find(path, target_dir):
    current_dir = os.path.abspath(path)
    if os.path.basename(current_dir) == target_dir:
        print(current_dir)
    try:
        dir_contents = os.listdir(current_dir)
    except FileNotFoundError:
        print(f"El directorio {current_dir} no existe.")
        return
    for item in dir_contents:
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            find(item_path, target_dir)
path = "./tree"
target_directory = "python"
find(path, target_directory)

