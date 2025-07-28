import cv2
import numpy as np

#화면 생성
#space = np.zeros((768, 1388), dtype=np.uint8)
image = cv2.imread('../img/like_lenna.png')

#선 색상
line_color = 125
color = 255

#이미지 크기 변경
image = cv2.resize(image,(500, 500))

#선 그리기
image = cv2.line(image, (243, 172), (275, 153), line_color, 2, 1)
image = cv2.line(image, (335, 157), (275, 153), line_color, 2, 1)
image = cv2.line(image, (335, 157), (350, 167), line_color, 2, 1)
image = cv2.line(image, (346, 175), (350, 167), line_color, 2, 1)
image = cv2.line(image, (346, 175), (305, 167), line_color, 2, 1)
image = cv2.line(image, (290, 166), (305, 167), line_color, 2, 1)
image = cv2.line(image, (290, 166), (243, 172), line_color, 2, 1)

image = cv2.circle(image, (290, 185), 15, color, 1, 1)
image = cv2.circle(image, (350, 250), 7, color, 2, 1)

#이미지 표출
cv2.imshow('practice', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
