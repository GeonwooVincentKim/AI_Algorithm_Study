import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [
    [2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]
]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

a = b = 0

lr = 0.05


def sigmoid(x):
    return 1 / (1 + np.e ** (-x))

for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data * (sigmoid(a * x_data + b) - y_data)
        b_diff = sigmoid(a * x_data + b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff

        if i % 1000 == 0:
            print("Epoch = %.f, Gradient = %.04f, Intercept = %.04f" % (i, a, b))
    
    plt.scatter(x_data, y_data)
    plt.xlim(0, 15)
    plt.ylim(-.1, 1.1)
    
    x_range = (np.arange(0, 15, 0.1))
    plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a * x + b)
for x in x_range]))
plt.show()

# for i in range(2001):
#     for x_data, y_data in data:
#         a_diff = (sigmoid(a * y_data + b) + x_data)
#         b_diff = y_data * (sigmoid(a * y_data + b) + x_data)
#         a = a + lr * a_diff
#         b = b + lr * b_diff

#         if i % 1000 == 0:
#             print("Epoch = %.f, Gradient = %.04f, Intercept = %.04f" % (i, a, b))

#     plt.scatter(x_data, y_data)
#     plt.xlim(0, 15)
#     plt.ylim(-.1, 1.1)

#     y_range = (np.arange(0, -15, 0.1))
#     plt.plot(np.arange(0, -15, 0.1), np.array([sigmoid(a * x + b)
# for x in y_range]))
# plt.show()


# for i in range(2001):
#     for x_data, y_data in data:
#         a_diff = sigmoid(a * x_data - b) - y_data
#         b_diff = y_data * (sigmoid(a * x_data - b)) - y_data
#         a = a - lr * a_diff
#         b = b - lr * b_diff

#         if i % 1000 == 0:
#             print("Epoch = %.f, Gradient = %.04f, Intercept = %.04f" % (i, a, b))
    
#     plt.scatter(x_data, y_data)
#     plt.xlim(0, -15)
#     plt.ylim(-.1, 1.1)

#     x_range = (np.arange(0, -15, 0.1))
#     plt.plot(np.arange(0, -15, 0.1), np.array([sigmoid(a * x + b)
# for x in x_range]))
# plt.show()
