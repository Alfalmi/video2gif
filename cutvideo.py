# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("video_2021-05-18_20-00-21.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# cutting out some part from the clip
# clip = clip.cutout(3, 10)


clip.write_gif("pinolargo.gif", fps=10)
# showing  clip
clip.ipython_display(width=120)

