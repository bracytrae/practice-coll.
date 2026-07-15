# gif-using-python
# this script creates a GIF animation from a set of image frames.

import imageio  # library used to read images and create GIFs

# this works when the images are stored locally on your computer.

# a list of image files that will become frames in the GIF
images = ["frame1.png", "frame2.png", "frame3.png"]

# Create a GIF file named "my_animation.gif" preferably 

# mode="I" allows multiple frames
# duration=0.5 every frame shows for 0.5 seconds
with imageio.get_writer("my_animation.gif", mode="I", duration=0.5) as writer:
    
    # loops through each image file
    for filename in images:
        
        # Reads the image file into memory
        frame = imageio.imread(filename)
        
        # Adds the image as a frame in the GIF
        writer.append_data(frame)
