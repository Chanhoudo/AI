from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import SGD
import cv2
import numpy as np

# 모델 경로
model_path = 'shape_recg.h5'

# 커스텀 객체 정의
custom_objects = {'SGD': SGD}

# 모델 로드
model = load_model(model_path, custom_objects=custom_objects)

# Test model on image
dir_path = 'Picture_Paint/four-shapes/shapes/circle/2.png'
test_img = cv2.imread(dir_path)
test_img = cv2.resize(test_img, (200, 200))  # 이미지를 모델 입력 크기로 리사이즈
test_img = test_img.reshape(1, 200, 200, 3)
Y = model.predict(test_img)[0]
val = np.argmax(Y)

# 결과 출력
if val == 0:
    print("Circle")
elif val == 1:
    print("Square")
elif val == 2:
    print("Star")
else:
    print("Triangle")