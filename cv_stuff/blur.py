### here I am comparing 2 approches to gaussian blur ###
### Now what the fuck is gaussian blur : bluring an image using a gaussian function to recduce noise level ###
### Just a disclamer these filters are very low level filters !

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

test_image = np.random.rand(5,5)
def conv(image,kernel):
    image_size = int(((image.shape[0] - kernel) / 1) + 1)
    ### (W - Kernel + 2*Padding) / Stride + 1
    print(f"new_image_size:{image_size}, Kernel: {kernel}")
    blured = []
    for i in range(image_size):
        for j in range(image_size):
            try:
                temp = image[0+i:kernel+i, 0+j:kernel+j]
                blured.append(temp.mean())      
            except exception as e:
                print(e)

    return image_size, blured

def padding():
    pass

def image_processing():
   img = Image.open("sample.jpg") 
   #print(np.array(img)[:,:,0])
   #plt.imshow(np.array(img)[:,:,0], cmap="gray")
   return np.array(img)[:,:,0]

### Okay so just for the sake of blurring things we will first look at Mean Blur 
### 1   1   1
### 1   1   1
### 1   1   1
def Mean_Blur(kernel = 16):
    image = image_processing()
    print(image.shape)
    image_size, blured_image = conv(image, kernel)
    new_image = np.array(blured_image).reshape(image_size, image_size)
    #print(new_image)
    plt.imshow(new_image, cmap = "gray")
    plt.show()

### 1   2   1
### 2   4   2
### 1   2   1
def Gaussian(kernel = 3):
    pass

Mean_Blur()

