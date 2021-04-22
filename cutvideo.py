# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("WR-104.mp4")


# getting only first 5 seconds
clip = clip.subclip(347, 355)

# cutting out some part from the clip
# clip = clip.cutout(3, 10)


clip.write_gif("mygif.gif", fps=5)
# showing  clip
clip.ipython_display(width=120)

