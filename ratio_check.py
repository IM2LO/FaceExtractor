import cv2
import os
from tqdm import tqdm

def move_images_with_incorrect_ratio(folder_path, target_folder):
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    
    image_files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    
    progress_bar = tqdm(total=len(image_files), desc="Checking...", unit="image")

    
    for image_path in image_files:
        
        image = cv2.imread(image_path)

        
        height, width, _ = image.shape
        ratio = width / height

        if ratio != 1.0:
            
            output_path = os.path.join(target_folder, os.path.basename(image_path))
            os.rename(image_path, output_path)

        
        progress_bar.update(1)

    
    progress_bar.close()


source_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces-cropped")


unsuccessful_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unsuccessful")


move_images_with_incorrect_ratio(source_folder, unsuccessful_folder)
