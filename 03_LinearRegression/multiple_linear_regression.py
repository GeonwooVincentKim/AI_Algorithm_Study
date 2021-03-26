import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time


print("1. 국어\n3. 영어\n5. 수2\n6. 미적분")
a1 = int(input("원하는 과목 별 번호를 입력하세요 : "))

time.sleep(0.5)

a2 = int(input("당신이 이번 시험을 준비하기 위해 썼던 시간을 적어주세요 : "))

time.sleep(0.5)

print("1. 국어\n3. 영어\n5. 수2\n6. 미적분")
b = int(input("원하는 과목의 점수를 입력하세요 : "))

# fake_data = [3, 76]
fake_data = []
fake_data.append(a1)
fake_data.append(a2)
fake_data.append(b)
print(fake_data)

current_data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
current_data.append(fake_data)
print(current_data)
x1 = [i[0] for i in current_data]
x2 = [i[1] for i in current_data]
y = [i[2] for i in current_data]

ax = plt.axes(projection='3d')
ax.set_xlabel('study_hours')
ax.set_ylabel('private_class')
ax.set_zlabel('Score')
ax.dist = 11
ax.scatter(x1, x2, y)
plt.show()

x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)

lr = 0.03

epochs = 2001

for i in range(epochs):
    y_pred = a1 * x1_data + a2 * x2_data + b
    error = y_data - y_pred
    a1_diff = - (2 / len(x1_data)) * sum(x1_data * (error))
    a2_diff = - (2 / len(x2_data)) * sum(x2_data * (error))
    b_diff = - (2 / len(x1_data)) * sum(y_data - y_pred)

    a1 = a1 - lr * a1_diff
    a2 = a2 - lr * a2_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("Epoch = %.f, 기울기-1 = %.04f, 기울기-2 = %.04f, 절편 = %.04f : " % (i, a1, a2, b))
