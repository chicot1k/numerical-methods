# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import numpy as np
import matplotlib.pyplot as plt

y10 = y20 = y40 = 1#задаем начальные условия
y30 = -2
a = 0
b = 5


def otv(x):#возвращает точное значение
    Y = [0, 0, 0, 0]
    Y[0] = math.exp(math.sin(x * x))
    Y[1] = math.exp(3 * math.sin(x * x))
    Y[2] = -1 * math.sin(x * x)-2
    Y[3] = math.cos(x * x)
    return Y


def f(x, Y):#ф от икс
    otv = []
    otv.append(2 * x * (abs(Y[1]) ** (1.0 / 3.0) * np.sign(Y[1])) * Y[3])
    otv.append(6 * x * math.exp(3.0 / -1.0 * (Y[2] + 2)) * Y[3])
    otv.append(-2 * x * Y[3])
    try:#логарфим если отрицательное
        otv.append(-2 * x * math.log(Y[0]))
    except:
        print("Горим!")
    return otv
def m(a, b):#функция евклидово расстаяние между двумя векторами
    otv = 0
    for i in range(len(a)):
        otv += (b[i] - a[i]) ** 2
    return otv ** (0.5)

def my(h):
    Y = [y10, y20, y30, y40]#по моей расчетной схеме
    Y_new = [0, 0, 0, 0]
    Y1 = [y10, y20, y30, y40]#по оппоненте 
    Y1_new = [0, 0, 0, 0]
    X = []
    Pog = []
    Pog1 = []
    x = a
    while x <= b+0.0001:#один шаг этого цикла
        K1 = [h * j for j in f(x, Y)]
        K2 = [h * z for z in f(x + 0.8 * h, [Y[j] + 0.8 * K1[j] for j in range(4)])]
        for i in range(4):
            Y_new[i] = Y[i] + 3.0 / 8.0 * K1[i] + 5.0 / 8.0 * K2[i]
        Y = Y_new[:]
        K1 = f(x, Y)
        K2 = f(x + 1.0/3.0 * h, [Y[j] + 1.0/3.0 * h * K1[j] for j in range(4)])
        K3 = f(x + 2.0/3.0 * h, [Y[j] + 2.0/3.0 * h * K2[j] for j in range(4)])
        for i in range(4):
            Y1_new[i] = Y1[i] + h * (1.0 / 6.0 * K1[i] + 4.0 / 6.0 * K2[i] + 1.0 / 6.0 * K3[i])
        Y1 = Y1_new[:]
        x += h
        X.append(x)
        Pog.append(-1 * math.log10(m(Y, otv(x))))
        Pog1.append(-1 * math.log10(m(Y1, otv(x))))
    fig = plt.subplots()
    plt.plot(X, Pog)
    plt.plot(X, Pog1)
    plt.show()
    print(Y)
    return Y



n = 6  # количетсво графиков
n_min = 7  # начиная с какой степени (нет проблем от 7)
Y = []
X = [k for k in range(n)]
for k in range(n):
    print(1.0 / (2.0 ** (n_min + k)))
    Y.append(m(my(1.0 / (2.0 ** (n_min + k))), otv(b)))
fig = plt.subplots()
plt.plot(X, Y)
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
