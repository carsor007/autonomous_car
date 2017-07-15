import matplotlib.pylot as plt
import matplotlib.image as mpimg
import numpy as np

#Read the image and print out some stats

image = mpimg.imread('test.jpg')
print('This image is: ',type(image),
        'with dimensions: ', image.shape)


# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

# Note: always make a copy rather than simply using "="
color_select = np.copy(image)

# Define our color selection criteria and populate rgb_threshold with these values.

red_threshold = 0
green_threshold = 0
blue_threshold = 0

####
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

#select any pixels below the threshold and set them to zero, retain those above threshold
# Do a boolean with the "|" character to identify
# pixels below the threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]  \
            | (image[:,:,2] < rgb_threshold[2])
color_select[thresholds] = [0,0,0]

#Display the Image
plt.imshow(color_select)
plt.show()
