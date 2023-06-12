import os
from tqdm import tqdm

def rename_files(folder_path):
    
    if not os.path.exists(folder_path):
        print("Specified folder doesn't exist.")
        return

    
    files = os.listdir(folder_path)

    
    files.sort()

    
    progress_bar = tqdm(total=len(files), desc="Naming...", unit="file")

    
    for index, file_name in enumerate(files):
        file_path = os.path.join(folder_path, file_name)
        new_file_name = str(index + 1) + os.path.splitext(file_name)[1]
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)

        
        progress_bar.update(1)

    
    progress_bar.close()


folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract-result")


rename_files(folder_path)
