import cv2
import os
from tqdm import tqdm
import config_manager


config = config_manager.read_config()


interval = int(config.get('interval', '10'))

def extract_frames(video_path, interval):
    
    video = cv2.VideoCapture(video_path)
    success, image = video.read()
    count = 0

    
    if not success:
        print(f"Failed to open video : {video_path}")
        return

    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract-result")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    progress_bar = tqdm(total=total_frames, desc=f"Shredding... {os.path.basename(video_path)}", unit="frame")

    
    while success:
        
        if count % interval == 0:
            output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_path))[0]}_frame_{count}.jpg")
            cv2.imwrite(output_path, image)

        success, image = video.read()
        count += 1

        
        progress_bar.update(1)

    
    video.release()
    progress_bar.close()

def process_videos_in_folder(folder_path, interval):
    
    video_files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file)) and file.endswith((".mp4", ".avi", ".mov", ".mkv"))
    ]

    
    for video_path in video_files:
        extract_frames(video_path, interval)


video_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")


process_videos_in_folder(video_folder, interval)
