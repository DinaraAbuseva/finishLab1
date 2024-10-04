import os 
import time 


line = " " * 20
frames = [
    f"\x1b[48;5;1m{line}\x1b[0m", 
    f"\x1b[48;5;7m{line}\x1b[0m", 
    f"\x1b[48;5;18m{line}\x1b[0m"
    ]
def animation(frames):
    for frame in frames:
        print(frame, end = "\r")
        time.sleep(0.5)
        os.system("cls")


while True:
    animation(frames)