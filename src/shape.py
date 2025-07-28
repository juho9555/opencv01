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

#화면에 선 좌표설정
#space = cv2.line(space, (100, 100), (800, 400), line_color, 3, 1)
#space2 = cv2.circle(space, (600, 200), 100, color, 4, 1)
#space3 = cv2.rectangle(space, (500, 200), (800, 400), color, 5, 1)
#space4 = cv2.ellipse(space, (500, 300), (300, 200), 0, 90, 250, color, 4)


image = cv2.line(image, (243, 172), (275, 153), line_color, 2, 1)
image = cv2.line(image, (335, 157), (275, 153), line_color, 2, 1)
image = cv2.line(image, (335, 157), (350, 167), line_color, 2, 1)
image = cv2.line(image, (346, 175), (350, 167), line_color, 2, 1)
image = cv2.line(image, (346, 175), (305, 167), line_color, 2, 1)
image = cv2.line(image, (290, 166), (305, 167), line_color, 2, 1)
image = cv2.line(image, (290, 166), (243, 172), line_color, 2, 1)

image = cv2.circle(image, (290, 185), 15, color, 1, 1)
image = cv2.circle(image, (350, 250), 7, color, 2, 1)



#격자 생성
#grid_spacing = 50
#grid_color = 225

#for x in range(0, image.shape[1], grid_spacing):
#    cv2.line(image, (x, 0), (x, image.shape[0]), grid_color, 1)

#for y in range(0, image.shape[0], grid_spacing):
#    cv2.line(image, (0, y), (image.shape[1], y), grid_color, 1)

#obj1 = np.array([[300, 500], [500, 500], [400, 600], [200,600]])
#obj2 = np.array([[600, 500], [800, 500], [700, 200]])
#space5 = cv2.polylines(space, [obj1], True, color, 3)
#space5 = cv2.fillPoly(space, [obj2], color, 1)
cv2.imshow('practice', image)

#cv2.imshow('line', space)
#cv2.imshow('line', space2)
#cv2.imshow('line', space3)
#cv2.imshow('line', space5)


cv2.waitKey(0)
cv2.destroyAllWindows()
