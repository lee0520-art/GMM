import ffmpeg
import json
import subprocess
import os
import sys
import time
import sys

def loudnorm(name, ext):
    singlePass = subprocess.Popen(
        (
            ffmpeg
            .input(f"{name}{ext}")
            .audio.filter("loudnorm", I=-16, TP=-1.5, LRA=11, print_format="json")
            .output("-", format="null")
            .global_args("-loglevel", "info")
            .global_args("-nostats")
            .global_args("-hide_banner")
            .compile()
        ),
        stderr=subprocess.PIPE
    )
    output = "\n".join(singlePass.communicate()[-1].decode("UTF-8").split("\n")[-8:-1])
    print(type(output))
    print(output)
    data = json.loads(output)

    measured_I = data["input_i"]
    measured_TP = data["input_tp"]
    measured_LRA = data["input_lra"]
    measured_thresh = data["input_thresh"]
    offset = data["target_offset"]

    (
        ffmpeg
        .input(f"{name}{ext}")
        .audio.filter("loudnorm", I=-16, TP=-1.5, LRA=11, measured_I=f"{measured_I}", measured_TP=f"{measured_TP}", measured_LRA=f"{measured_LRA}", measured_thresh=f"{measured_thresh}", offset=f"{offset}")
        .output(f"output/{name}.m4a", format="mp4", acodec="aac")
        .global_args("-ar", "48k")
        .global_args("-vbr", "5")
        .global_args("-loglevel", "quiet")
        .global_args("-nostats")
        .global_args("-hide_banner")
        .run()
    )
    return
    
voices="test.wav"

sys.argv.append("voices")
print(sys.argv)
if len(sys.argv) < 2:
    sys.exit("[Error] Path required!")

try:
    os.chdir(os.path.join("C:\\Users\\user\\SpeakerRecognition_tutorial_",sys.argv[1]))
except:
    sys.exit(f"[Error] Not a directory: {sys.argv[1]}")

os.makedirs("./output", exist_ok=True)

audioFiles = [".mp3", ".m4a", ".wav", ".aiff", ".flac", ".ogg"]
files = os.listdir(os.path.join("C:\\Users\\user\\SpeakerRecognition_tutorial_",sys.argv[1]))
print(files)
print("ffmpeg loudnorm started")
for file in files:
    name, ext = os.path.splitext(file)
   
    
    if ext in audioFiles:
        print(f"Processing {name}{ext}", end=" ", flush=True)
        startTime = time.time()
        loudnorm(name, ext)
        endTime = time.time()
        print(f"... Complete! ({round(endTime - startTime, 1)} sec)")
    else:
        print(f"{name}{ext} is not audio files. skipped.")