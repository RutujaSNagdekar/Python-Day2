import matplotlib.image as mi
import matplotlib.pyplot as mp
from PIL import Image
image_path = "1.png"

# Read/Load Image and coverted into numpyarray
img = mi.imread(image_path)    #import matplotlib.image as mi
print(type(img))

# Extract the dimentions (height, width, channels)

print(img.shape)

# To print the image in the form of numpy array

print(img)

# To display the image from numpy array

mp.imshow(img)    #import matplotlib.pyplot as mp
mp.show()
