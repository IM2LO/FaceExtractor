import cv2
import dlib
import os
from tqdm import tqdm
import config_manager


config = config_manager.read_config()


margin = int(config.get('margin', '50'))
size = int(config.get('size', '512'))

def crop_faces(folder_path, output_folder, size, margin):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    num_images = len(os.listdir(folder_path))

    
    progress_bar = tqdm(total=num_images, desc="Cropping...", unit="image")

    
    detector = dlib.get_frontal_face_detector()

    
    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)

        
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        
        faces = detector(gray_image)

        
        for face in faces:
            
            left = max(0, face.left() - margin)
            top = max(0, face.top() - margin)
            right = min(image.shape[1], face.right() + margin)
            bottom = min(image.shape[0], face.bottom() + margin)

            
            if right - left >= size and bottom - top >= size:
                
                cropped_image = image[top:bottom, left:right]

                
                resized_image = cv2.resize(cropped_image, (size, size))

                
                output_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_path, resized_image)

        
        progress_bar.update(1)

    
    progress_bar.close()


faces_detected_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces-detected")


faces_cropped_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces-cropped")


crop_faces(faces_detected_folder, faces_cropped_folder, size, margin)
