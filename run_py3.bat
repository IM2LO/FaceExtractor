@echo off
python3 config_displayer.py
python3 shredder.py
python3 pics_naming_results.py
python3 faces_detector.py
python3 faces_crop.py
python3 ratio_check.py
python3 pics_naming_cropped.py
pause
