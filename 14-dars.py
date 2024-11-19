num = float(input("Sonni kiriting: "))
percen = float(input("Foizni kiriting: "))
result = num + (num * (percen / 100))

print(result)

height = float(input("Bo'yingizni kiriting: "))
weigth = float(input("Vazningizni kiriting: "))
mes = weigth / height ** 2

if mes < 18.5:
  print("Sizning vazningiz yetarli emas!")
elif mes < 25:
  print("Sizning vazningiz yetarli!")
elif mes < 30:
  print("Sizning vazningiz ortiqcha!")
else:
  print("Siz semirib ketibsiz!")

num = 1.7671

print(round(num, 1))
print(round(num, 3))

n = float(input("Kuchni kiriting: "))
n *= 10

print(int(n))

x = float(input("X kordinatani kiriting: "))
y = float(input("Y kordinatani kiriting: "))
x *= 10
y *= 10

print(int(x), int(y))

import math

x = float(input("X kordinatani kiriting: "))
y = float(input("Y kordinatani kiriting: "))
dis = math.sqrt((x ** 2) + (y ** 2))

print(round(dis, 2))

import math

dis = float(input("Masofani kiriting: "))
angle = float(input("Burchakni kiriting: "))
angle /= 57.2958
x = math.cos(angle) * dis
y = math.sin(angle) * dis

print("Kordinatalar: ", x, ";", y)

import math

a = float(input("Sonni kiriting: "))

print(math.floor(a))
print(math.ceil(a))