# Improting Image class from PIL module 
from PIL import Image 

# Opens a image in RGB mode 
im = Image.open('ticko_for_qr.jpg') 

# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 
print(width, height)

# Setting the points for cropped image 
left = 30
top = 18
right = 100
bottom = 100
print(left, top, right, bottom)
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
im1.show() 
