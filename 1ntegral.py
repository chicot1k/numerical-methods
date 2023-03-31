# coding=utf-8
# This is a sample Python script.

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
def f(x):
  return 3.5*math.cos(0.7*x)*math.e**(-5*x/3.0) + 2.4*math.sin(5.5*x)*math.e**(-3*x/4.0) + 5
def ff(x):
  return f(x)/((x-1.1)**0.8*(2.3-x)**(0))
def J(x,a,b):
  alpha = 0.8
  beta = 0
  return f(x)/(((x-a)**alpha)*((b-x)**beta))
a = 1.1
b = 2.3
v, err = integrate.quad(ff, a, b)
def mu(k,st,ed):
  return (ed-a)**(k+0.2)/(k+0.2)-(st-a)**(k+0.2)/(k+0.2)
def NK1(n,st,ed):
  X = np.linspace(st,ed,n)#получаем список узлов(разбиение)
  T = [_ - a for _ in X]#перевожу все иксы в базиз т
  A = np.eye(n)#создаю единичную матрицу
  for i in range(n):
    for j in range(n):
      A[i][j] = T[j]**i#задаю левую часть систему с узлами
  B = []
  for i in range(n):
    B.append(mu(i,st,ed))#формиррование правой части с моментами
  Aj = np.linalg.solve(A,B)#решение системы
  otv = 0
  for i in range(n):
    otv += Aj[i]*f(a+T[i])#Квадратурная формула
  sumAj = 0
  for i in range(n):
    sumAj += abs(Aj[i])#Cумма модулей коэффициентов
  return [otv,sumAj]
def NK(h,st,ed):
  X = [] #пустой список
  q = st #начало
  while q<=ed+0.0001:#массив узлов
    X.append(q) #в массив вставляет узлы
    q+=h #шаг узла
  n = int(round((ed-st)/h)+1) #колво узлов
  T = [_ - a for _ in X] #переход к новому базису t
  TA = np.eye(n) #единичная матрица
  for i in range(n):
    for j in range(n):
      TA[i][j] = T[j]**i #формируем матрицу тэшек
  B = []
  for i in range(n):
    B.append(mu(i,st,ed)) #формируем столбец мюшек
  Aj = np.linalg.solve(TA,B) #решаем
  otv = 0
  for i in range(n):#сумма ищем приблеженное значение
    otv += Aj[i]*f(T[i]+a)
  return otv #результат
def GS(h,st,ed):
  X = [] #задаем пустой массив
  q = st #начало
  while q<=ed+0.0001: # задаем узлы
    X.append(q) #заполняем массив узлами
    q+=h #прибавляем к началалу шаг
  n = int(round((ed-st)/h)+1) #считаем количество узлов
  T = [_ -a for _ in X] #переходим к базису t
  A = np.eye(n) #создаем единичный массив
  for i in range(n):
    for j in range(n):
      A[i][j] = mu(i+j,st,ed)#заполняем матрицу моментами
  B = []#создаем пустой массив
  for i in range(n):
    B.append(-1*mu(n+i,st,ed)) #заполняем его моментами
  aj = np.linalg.solve(A,B) #находим aj для полинома
  aj = aj[::-1] #реверс в нужный порядок
  aj = np.insert(aj,0,1) # добавляем согласно полиному единичку
  T = np.roots(aj)#находим корни полинома
  TA = np.eye(n)#создаем единичную матрицу
  for i in range(n):
    for j in range(n):
      TA[i][j] = T[j]**i#заполняем матрицу тэшек
  B = []#Создаем пустой массив
  for i in range(n):
    B.append(mu(i,st,ed))#заполняем его моментами
  Aj = np.linalg.solve(TA,B)#решаем систему лин уравнений
  otv = 0
  for i in range(n):
    otv += Aj[i]*f(a+T[i])#составляем сумму
  return otv
def GS1(n,st,ed):
  A = np.eye(n)#создаем единичную матрицу
  for i in range(n):
    for j in range(n):
      A[i][j] = mu(i+j,st,ed)#формируем левую часть первой системы
  B = []
  for i in range(n):
    B.append(-1*mu(n+i,st,ed))#формируем правую часть первой системы
  aj = np.linalg.solve(A,B)#решаем
  aj = aj[::-1]#разворачиваем
  aj = np.insert(aj,0,1)#добавляю единицу в начало так как при решение полинома первой стоит единица
  T = np.roots(aj)#решение полинома
  A = np.eye(n)#формируем единичную матрицу
  for i in range(n):
    for j in range(n):
      A[i][j] = T[j]**i#формируем левую часть второй системы
  B = []
  for i in range(n):
    B.append(mu(i,st,ed))#формируем правую часть второй системы
  Aj = np.linalg.solve(A,B)#решение
  otv = 0
  for i in range(n):
    otv += Aj[i]*f(a+T[i])#квадратурная формула
  return otv
n = 7
X = [_ for _ in range(n)]#задем узлы
Y = [abs(GS1((_+1),a,b)-v) for _ in range(n)]#график абсолютной погрешности
n = 7
X= [_ for _ in range(n)]#задем узлы
Y1 = [abs(NK1(_+5,a,b)[0]-v) for _ in range(n)]
print(GS1(2,a,b))
print(NK1(2,a,b)[0])
fig = plt.subplots()
plt.plot(X,Y1)
plt.show()
def GSsost():
  ii = 0#номер итерации
  k = 2#начальное количество разбиений
  h = (b-a)/k#начальный шаг
  R=100 #оценка погрешности
  while R>eps:#пока оценка погрешности больше чем необходимое
    print(ii)#номер итерации
    ii+=1#уведичиваем счетчик
    print(k,h)#выводим начальное количество разбиений и шаг
    Sh1 = 0#инициализация
    Sh2 = 0
    Sh3 = 0
    X = []
    q = a
    while q<=b+0.0001:#задаем узлы
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh1 += GS1(3,X[i],X[i+1])#вычисляем по формуле кф типа гаусса
    # Sh1 = float(Sh1)
    X = []
    h = h/2
    q = a
    while q<=b+0.0001:
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh2 += GS1(3,X[i],X[i+1])
    # Sh2 = float(Sh2)
    X = []
    h = h/2
    q = a
    while q<=b+0.0001:
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh3 += GS1(3,X[i],X[i+1])
    # Sh3 = float(Sh3)
    m = abs(math.log(abs((Sh3-Sh2)/(Sh2-Sh1)))/math.log(2))#вычисляем m
    Cm = abs((Sh2-Sh3)/(h**m-(2*h)**m))#главный член погрешности
    h*=4
    R = abs(Sh2-Sh1)/(2**m-1)#оценка погрешности
    if h / (h/2*(eps/R)**(1/m)*0.95) > 3:#проверерят уменьшенее шага (для оптимального шага)
      h/=3
    else:
      h = h/2*(eps/R)**(1/m)*0.95
    k = round((b-a)/h)
    h = (b-a)/k
    print(h)
    print(m,Cm)
    print(R,abs(v-Sh2),eps)
def NK_sost():
  ii = 0
  k = 2
  h = (b-a)/k
  R=100
  while R>eps:
    print(ii)
    ii+=1
    print(k,h)
    Sh1 = 0
    Sh2 = 0
    Sh3 = 0
    X = []
    q = a
    while q<=b+0.0001:
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh1 += NK1(3,X[i],X[i+1])[0]
    # Sh1 = float(Sh1)
    X = []
    h = h/2
    q = a
    while q<=b+0.0001:
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh2 += NK1(3,X[i],X[i+1])[0]
    # Sh2 = float(Sh2)
    X = []
    h = h/2
    q = a
    while q<=b+0.0001:
      X.append(q)
      q+=h
    for i in range(len(X)-1):
      Sh3 += NK1(3,X[i],X[i+1])[0]
    # Sh3 = float(Sh3)
    m = abs(math.log(abs((Sh3-Sh2)/(Sh2-Sh1)))/math.log(2))
    Cm = abs((Sh2-Sh3)/(h**m-(2*h)**m))
    h*=4
    R = abs(Sh2-Sh1)/(2**m-1)#
    if h / (h/2*(eps/R)**(1/m)*0.95) > 3:
      h/=3
    else:
      h = h/2*(eps/R)**(1/m)*0.95
    k = round((b-a)/h)
    h = (b-a)/k
    print(h)
    print(m,Cm)
    print(R,abs(v-Sh2),eps)
eps = 10**(-10)
GSsost()
NK_sost()

