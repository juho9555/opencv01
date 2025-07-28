# 1-1. OpenCV 가상환경 설정

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
