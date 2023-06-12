import cv2
import os
import dlib
from tqdm import tqdm

def detect_faces(image_path):
    
    face_detector = dlib.get_frontal_face_detector()

    
    image = cv2.imread(image_path)

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    faces = face_detector(gray)

    return faces

def process_images_in_folder(folder_path):
    
    output_folder_face_detected = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces-detected")
    output_folder_unsuccessful = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unsuccessful")
    for output_folder in [output_folder_face_detected, output_folder_unsuccessful]:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    
    image_files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    
    progress_bar = tqdm(total=len(image_files), desc="Detecting...", unit="image")

    
    for image_path in image_files:
        
        faces = detect_faces(image_path)

        if len(faces) > 0:
            
            (x, y, w, h) = faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height()
            image_width = cv2.imread(image_path).shape[1]
            image_height = cv2.imread(image_path).shape[0]
            face_area = w * h
            image_area = image_width * image_height
            face_ratio = face_area / image_area

            if face_ratio >= 0.02:  
                
                output_path = os.path.join(output_folder_face_detected, os.path.basename(image_path))
                os.rename(image_path, output_path)
            else:
                
                output_path = os.path.join(output_folder_unsuccessful, os.path.basename(image_path))
                os.rename(image_path, output_path)
        else:
            
            output_path = os.path.join(output_folder_unsuccessful, os.path.basename(image_path))
            os.rename(image_path, output_path)

        
        progress_bar.update(1)

    
    progress_bar.close()


extract_result_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract-result")


process_images_in_folder(extract_result_folder)
