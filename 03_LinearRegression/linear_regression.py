import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
current_data.append(fake_data)
print(current_data)
x = [i[0] for i in current_data]
y = [i[1] for i in current_data]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

lr = 0.03

epochs = 2001

for i in range(epochs):
    y_pred = a * x_data + b
    error = y_data - y_pred
    a_diff = - (2 / len(x_data)) * sum(x_data * (error))
    b_diff = - (2 / len(x_data)) * sum(error)

    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("Epoch = %.f, 기울기 = %.04f, 절편 = %.04f" % (i, a, b))

y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()
