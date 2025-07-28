import cv2
import numpy as np

new_height = 300
new_width = 300

image = cv2.imread('../img/like_lenna.png')
#image_small = cv2.resize(image, (500,500))


dst = np.zeros((new_height, new_width), dtype=np.uint8)
dst = cv2.resize(image, (new_width, new_height))

cv2.resize(image, (new_width, new_height), dst=dst)

#이미지를 보여주는 명령어
cv2.imshow('Image Window', image)
cv2.imshow('Image Window', dst)

#cv2.imshow('Image Window', image_small)
print(image.shape)
#print(image_small.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()