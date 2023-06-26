import matplotlib.pyplot as plt
import numpy as np 
import os
import re

folder_path = "/home/ericlee/Pytorch-UNet/test_folder"
img_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
mask_files = [f for f in os.listdir(folder_path) if f .endswith(".png")]

img_files = sorted(img_files)
mask_files = sorted(mask_files)

print(img_files)
print(mask_files)
for img_file, mask_file in zip(img_files, mask_files):
    print(img_file)
    print(mask_file)
    img = plt.imread(os.path.join(folder_path, img_file))
    mask = plt.imread(os.path.join(folder_path, mask_file))

    x = np.arange(img.shape[1])
    y = np.arange(img.shape[0])
    X, Y = np.meshgrid(x, y)

    plt.contour(X, Y, mask, levels=[0.5], color='red', linewidth=2)

    plt.imshow(img, cmap="gray")

    plt.show()

