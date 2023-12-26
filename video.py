from moviepy.editor import *

clip1 = VideoFileClip("D:/08 Code\insToBili/：saved/2023-09-01_04-57-51_UTC.mp4", audio=True)
clip2 = VideoFileClip("D:/08 Code\insToBili/：saved/2023-09-10_04-41-52_UTC.mp4", audio=True)

final = concatenate_videoclips([clip1, clip2], method="compose")
final.write_videofile("D:/08 Code/insToBili\/est1.mp4")