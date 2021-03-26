import numpy as np
import time

print("1. 국어\n3. 영어\n5. 수2\n6. 미적분")
a = int(input("원하는 과목 별 번호를 입력하세요"))

time.sleep(0.5)

print("1. 국어\n3. 영어\n5. 수2\n6. 미적분")
b = int(input("원하는 과목의 점수를 입력하세요"))

# fake_data = [3, 76]
fake_data = []
fake_data.append(a)
fake_data.append(b)
print(fake_data)

current_data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in current_data]
y = [i[1] for i in current_data]

def predict(x):
    return fake_data[0] * x + fake_data[1]


def mse(y, y_hat):
    return ((y - y_hat) ** 2).mean()


def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))


predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부할 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" %
            (x[i], y[i], predict(x[i])))

print("Mse 최종 값 : " + str(mse_val(predict_result, y)))

# if __name__ == "__main__":
#     predict_result = []
    
#     for i in range(len(x)):
#         predict_result.append(predict(x[i]))
#         print("공부할 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" % (x[i], y[i], predict(x[i])))

#     print("Mse 최종 값 : " + str(mse_val(predict_result, y)))
