from moviepy.editor import *
from moviepy.video.fx import *
import os
import time

L = []
for root, dirs, files in os.walk("D:/08 Code/insToBili/：saved"):
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

timestr = time.strftime("%Y%m%d%H")
print(timestr)
final_clip = concatenate_videoclips(L, method="compose")
final_clip.to_videofile("D:/08 Code/insToBili/outputs/"+timestr+".mp4",fps=24)
