from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path_1 = '/home/ericlee/Breast/seg/masks/0_0_before_mask.png'
path_2 = '/home/ericlee/Pytorch-UNet/_data/masks/0cdf5b5d0ce1_01_mask.gif' 

img_1 = Image.open(path_1)
img_2 = Image.open(path_2)

img_1_np = np.array(img_1)
img_2_np = np.array(img_2)

print(np.unique(img_1_np))
print(np.unique(img_2_np))