import numpy as np

w11 = np.array([-2, -2])
w12 = np.array([2, 2])
w2 = np.array([1, 1])

b1 = 3
b2 = -1
b3 = -1


def MLP(x, w, b):
    y = np.sum(w * x) + b

    if y <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    MLP(np.array([-2, -2]), w11, b1)
    print(MLP(np.array([-2, -2]), w11, b1))
