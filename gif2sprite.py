#Gif2sprite gets all gif images in the directory and convert to a spritesheet
#Lucas 

import os
from PIL import Image

for im in os.listdir():
    #check if is a gif
    if im.endswith('.gif'):
        gif = Image.open(im)
        print(f"size : {gif.size}")
        print(f"frames : {gif.n_frames}")
        spritesheet = Image.new('RGBA',(gif.size[0]*gif.n_frames,gif.size[1]))
        #loops the frame and append to spritesheet
        for frame in range(gif.n_frames):
            gif.seek(frame)
            position = (gif.size[0]*frame, 0)
            spritesheet.paste(gif,position)
            pass
        #save the spritesheet
        spritesheet.save(im+".png")
    pass