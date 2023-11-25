import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D, Flatten, Dense
from openpyxl import load_workbook

#load_wb = load_workbook("/Users/hanjeonghyeon/Desktop/output.xlsx", data_only=True)
#ws = load_wb['Sheet1'] # load_w  b 는 시트를 불러오는것이고 s는 셀 주소를 말하는것임






# 입력 데이터 크기 및 형태
input_shape = (1000,)  # 입력 데이터의 크기에 맞게 수정해야 합니다.

# 오른쪽 입력
right_input = Input(shape=input_shape, name='right_input')
right_conv = Conv1D(32, kernel_size=3, activation='relu')(right_input)
right_pooling = MaxPooling1D(pool_size=2)(right_conv)

# 왼쪽 입력
left_input = Input(shape=input_shape, name='left_input')
left_conv = Conv1D(32, kernel_size=3, activation='relu')(left_input)
left_pooling = MaxPooling1D(pool_size=2)(left_conv)

# 병합
merged = tf.keras.layers.concatenate([right_pooling, left_pooling])

# 공통 레이어
flatten = Flatten()(merged)
dense = Dense(64, activation='relu')(flatten)
output = Dense(2)(dense)  # 출력층의 뉴런 수는 2로 설정하고, 적절한 활성화 함수를 선택해야 합니다.

# 모델 구성
model = Model(inputs=[right_input, left_input], outputs=output)

# 모델 컴파일
model.compile(loss='mse', optimizer='adam')  # 손실 함수와 옵티마이저는 상황에 맞게 선택해야 합니다.

# 모델 요약
model.summary()