
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "like_lenna.png"
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def rotate_image(image, angle, center=None):
    rows, cols, _ = image.shape
    if center is None:
        center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

rotated_img = rotate_image(img, 45)
plt.imshow(rotated_img)
plt.title("Rotated Image")
plt.show()
