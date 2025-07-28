import cv2

image = cv2.imread('../img/like_lenna.png')
image_small = cv2.resize(image, (500,500))

#이미지를 보여주는 명령어
#cv2.imshow('Image Window', image)
cv2.imshow('Image Window', image_small)
#print(image.shape)
print(image_small.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()