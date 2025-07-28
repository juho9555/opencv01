# OpenCV

## opencv에서 이미지 수치화가 중요한 이유
1. 이미지 처리 기능들이 수치 기반
2. AI에 넣기 위해 필수 (AI가 학습할 때 처리하는 속도 향상)
3. 객관적인 판단이 가능해짐 (명암이나 밝기등을 정확히 판별 가능)

### 해상도
- 해상도란 화면을 구성하는 가로 x 세로의 픽셀 수를 의미
- ex) 1920x1080 = 가로 1920픽셀, 세로 1080픽셀
- 픽셀수가 많을수록 선명하고 품질이 좋음
- HD, FHD, QHD, 4K등이 존재
  
### 색공간
- 그레이스케일 (명도만 존재)
- RGB (빨강, 초록, 파랑)
- CMYK (청록, 자홍, 노랑, 검정)
- HSV (색상, 채도, 명도)

### 비트(bit)
- 1 bit = 검정 또는 흰색
- 8 bit = 0부터 255(흰색)까지 표현가능
- 16 bit = 0 ~ 65535까지 표현가능 (색상이 더 부드러움)


## opencv 가상환경 설정

- project 폴더안에 opencv01폴더 생성
- opencv01 폴더에 img폴더와 src폴더 생성
- src에서 helloworld.py생성
- myvenv로 가상환경 설정 (용량 큼)
- opencv01에서 .gitignore파일 생성 후 myvenv를 제외하고 git에 업로드
- src에서 git init으로 git파일 생성
- git brance -m master main으로 ~/project/opencv01/src (master) -> ~/project/opencv01/src (main)으로 변경

```
import cv2

image = cv2.imread('../img/like_lenna.png')
cv2.imshow('Image Window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

- 위 코드를 helloworld.py에 입력 후 터미널창에서 python helloworld.py로 실행
- 실행 한 후 터미널창에서 git status로 상태확인하면 아직 Untracked상태임을 확인가능
- git add . 입력해 tracked상태로 변경
- git commit "~~"로 git에 설명추가
- github desktop 실행해 add new repository에서 /project/opencv01 파일 선택
- changes 확인하고 push하기
