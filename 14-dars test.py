# 1-vazifa

y = float(input("Xarid narxini yevroda kiriting: "))
rubl = y * 1.25 * 60.87

print("Xarid narxi", rubl, "rubl")

# 2-vazifa

import math

n = float(input("Sonni kiriting: "))

if n > 0:
  n = math.ceil(n)
  print("x = ", n)
  print("log(x) = ", math.log(n))
else:
  n = math.floor(n)
  print("x =", n)
  print("exp(x) = ", math.exp(n))

# 3-vazifa

import math

summ = 1
down = float(input("Yuklab olish uchun fayl hajmini kiriting: "))
speed = float(input("Ulanish tezligini kiriting: "))
percent = 100 / (down / speed)
percent = math.ceil(percent)

while  True:
  print(summ, "sekund o'tdi")
  print(down,"megabaytdan", speed, "megabayt yuklab olindi", percent, "%")
  if speed == down:
    break
  speed += speed
  percent += percent
  summ += 1

# 4-vazifa

x = float(input("Musbat haqiqiy sonni kiriting: "))
birinchi_raqam = int(x * 10) % 10

print(birinchi_raqam)

# 5-vazifa

import math

yer_hajmi = 10.8321 * (10**11)
r = float(input("Tasodifiy sayyora radiusini kiriting: "))
v = 4 / 3 * math.pi * r ** 3

if v < yer_hajmi:
  print("Yer sayyorasining hajmi: ", round(yer_hajmi / v,3), "marta katta")
else:
  print("Yer sayyorasining hajmi: ", round(v / yer_hajmi,3), "marta kichik")

# 6-vazifa

low_chegara = int(input("Quyi harorat chegarasini kiriting: "))
high_chegara = int(input("Yuqori harorat chegarasini kiriting: "))
step = int(input("Qadamni kiriting: "))

print("C", "F")

for c in range(low_chegara,high_chegara+1,step):
  f = c * 1.8 + 32
  print(c, f)

print(high_chegara, high_chegara * 1.8 + 32)

# 7-vazifa

x_ot = float(input("Otning turgan joyini kiriting: "))
y_ot = float(input("Otning turgan joyini kiriting: "))
x_nuqta = float(input("Doskadagi turgan nuqtaning joyini kiriting: "))
y_nuqta = float(input("Doskadagi turgan nuqtaning joyini kiriting: "))
x_ot = int(x_ot * 10)
y_ot = int(y_ot * 10)

print("Qafasdagi ot ", x_ot, ",", y_ot)

x_nuqta = int(x_nuqta * 10)
y_nuqta = int(y_nuqta * 10)

print("Qafasdagi nuqta ", x_nuqta, ",", y_nuqta)

if x_ot != x_nuqta and y_ot != y_nuqta:
  print("Ha, ot bu nuqtaga yura oladi")
else:
  print("Yo'q, ot bu nuqtaga yura olmaydi")

# 8-vazifa

import math

a = float(input("Boshlang'ich burchak gradusini kiriting: "))
a /= 57.2958
hour = float(input("Soatni kiriting: "))
oxirgi_burchak = (a + 30 * hour) % 360

print("Oxirgi soat boshidan minut strelkasi ", round(oxirgi_burchak, 1), "burchakka burilgan")

# 9-vazifa

import math

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
d = b ** 2 - 4 * a * c

if d > 0:
  x1 = (-b + math.sqrt(d)) / (2 * a)
  x2 = (-b - math.sqrt(d)) / (2 * a)
  print("Tenglama ikkita ildizga ega: ", x1, "va", x2)
elif d == 0:
  x = -b / (2 * a)
  print("Tenglama bitta ildizga ega: ", x)
else:
  print("Tenglama ildizga ega emas")

# 10-vazifa

import math

a = float(input("Sonni kiriting: "))
b = float(input("Sonni kiriting: "))
eng_katta_son = (a + b + abs(a - b)) / 2

print("Eng katta son: ", eng_katta_son)