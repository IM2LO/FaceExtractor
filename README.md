# Face Extractor
Little configurable thing to bulk extract faces from several videos at once.

**Retrieve, Detect, Crop.**

Everything works in one-click, scripts are automatically launched in the right order.

**MP4, AVI, MKV, MOV files supported.**

Face Extractor allows you to collect datas to feed neural networks-based AIs like Stable Diffusion, DeepFaceLab and so on...

***Runs on Windows and Mac***
## Guidelines

***Python 3.10.6+***

Get it from [here](https://www.python.org/downloads/release/python-3106/).

**NVIDIA graphics card with CUDA support** is highly recommended for fastest result, but not necessary... Unless you have a good CPU.

*Tip: As this program is fairly tiny, it would rather not cause any issue if you run it outside a virtual environment, but you still can do it. This will not be covered here.*
## Installation

1. Download the repo with a simple git request.

```bash
  git clone https://github.com/IM2LO/FaceExtractor/
```
2. Then enter the downloaded folder, create a ***videos*** folder among the scripts (don't forget the **s**).

3. Start a terminal within the folder and install the requirements with a **pip** command like this :
```bash
  pip install -r requirements.txt
```

4. There's no 4, you're done!


## How To Use

1. Copy your videos to the *videos* folder.

*Tip: Pre-editing your videos is recommended to maximize the chances of a successful result. It's also best to have at least FullHD resolution videos (usually 1920x1080).*

2. Configure the program by modifying the values in the *config.txt* file. You can tweak the frame saving interval, the margin around the faces and the size of the resulting images.

*Tip: If you set no values in the config file, it will run with the default configuration, which is : frame captured each 10, margin of 50px around faces, 512x512px outputs images.*

3. a. On **Windows**, open the .bat file corresponding to your version of Python (run_py3.bat will launch each script with the command "python3", run.bat will launch each script with the command "python").

b. On **MacOS**, open a terminal in the folder and run one of the two following commands, depending on your version of Python:
```bash
./run_py3.sh
./run.sh
```
run_py3.sh will launch each script with the "python3" command, run.sh will launch each script with the "python" command.

4. Let the program run.

5. The result will be available in the *faces-cropped* directory.

6. ***Check*** the data afterwards, wrong faces or errors could happen sometimes.

You noticed there's an *unsuccessful* folder automatically created, it contains every picture that seems to have no faces in it. As the program may fail, you can scroll down this folder and get wrongly unsuccessful pictures back in the dataset (but you have to crop it by hand)


## Final Note

Improvements will surely come, need to work on face recognition and sorting, better detection too... It's not perfect yet but it can still save a huge amount of time. The intention was to make a one-click easy-to-use and easy-to-setup ready-made program that can suit both newbies and pros.

Please use the extracted faces in a respectful, non-discriminatory way. I take no responsibility for any misuse of this program.

