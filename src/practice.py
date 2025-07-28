import cv2
import numpy as np

#이미지 가져오기
image = cv2.imread('../img/like_lenna.png')

#이미지 크기 설정
height, width, channels = image.shape

#배율로 사이즈 변환
#image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

#대칭 변환 (0이면 반전, 1이면 정상)
#image_fliped = cv2.flip(image, 0)

#이미지 회전 (width/2, height/2) = center, 90 = angle, 1 = scale
#center = 회전의 중심 좌표 (x,y). angle은 각도. scale은 이미지 확대/축소 비율
#matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
#(src, M, dsize). src = 원본 이미지. M = 변환 행렬(2x3). dsize = 출력 이미지 크기(가로, 세로)
#result = cv2.warpAffine(image, matrix, (width, height))

croped_image = image[50:150,50:150]
croped_image[:] = 200


#이미지 보여줌
#cv2.imshow('Image_Window', image_big)
#cv2.imshow('Image_Window', image_fliped)
#cv2.imshow('Image_Window', result)
cv2.imshow('Image_Window', image)

#이미지 창 유지
cv2.waitKey(0)
cv2.destroyAllWindows()