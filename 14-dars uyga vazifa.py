# 1-vazifa

rubl = float(input("Qancha rubl tikamiz: "))
k = float(input("Koeffisient qanday: "))

print("Potensial yutuq: ", round(rubl * k, 2))

# 2-vazifa

c = float(input("Haroratni kiriting: "))
age = float(input("Yoshingizni kiriting: "))
summ = (age * (1.5 + c))

print("Ota og'liga shuncha pul so'vg'a qiladi: ", summ)

# 3-vazifa

height = float(input("Bo'yingizni kiriting: "))
weigth = float(input("Vazningizni kiriting: "))
mes = weigth / height ** 2
mes = round(mes,2)

if mes < 18.5:
  print("Sizning vazningiz yetarli emas!")
elif mes < 25:
  print("Sizning vazningiz yetarli!")
elif mes < 30:
  print("Sizning vazningiz ortiqcha!")
else:
  print("Siz semirib ketibsiz!")

# 1-vazifa

ch = float(input("Chatllar sonini kiriting: "))
cr = int(ch / 2200)

print("Bu", cr, "CR")
print("Korabllar sotib olish mumkin: ", int(cr / 0.5))

# 2-vazifa

print("Donaning joylashgan o'rnini kiriting: ")

g = float(input("Gorizontal bo'yicha: "))
v = float(input("Vertikal bo'yicha: "))

if 0 < g < 0.8 and 0 < v < 0.8:
  g = int(g * 10)
  v = int(v * 10)
  print("Dona", (g, v), "katakda joylashgan")
else:
  print("Bunday koordinatali katak yo'q!")

# 1-vazifa

a = float(input("Uchburchakning birinchi tomonini kiriting: "))
b = float(input("Uchburchakning ikkinchi tomonini kiriting: "))
c = float(input("Uchburchakning uchinchi tomonini kiriting: "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))

print("Uchburchakning yuzi: ", s)

# 2-vazifa

import math

dis = float(input("Masofani kiriting: "))
angle = float(input("Burchakni kiriting: "))
angle /= 57.2958
x = math.cos(angle) * dis
y = math.sin(angle) * dis

print("Kordinatalar: ", x, ";", y)

# 3-vazifa

import math

n = float(input("Sonni kiriting: "))

print("Modul: ", abs(n))
print("Sonni pastga qarab yaxlitlash: ", math.floor(n))
print("Sonni yuqoriga qarab yaxlitlash: ", math.ceil(n))
print("Sonni kvadrat ildizini hisoblash: ", math.sqrt(n))
print("Sonni eksponentasi: ", math.exp(n))
print("Sonni factorialini hisoblash: ", math.factorial(n))
print("Sonni logarifmini hisoblash: ", math.log(n))
print("Sonni logarifmini hisoblash: ", math.log2(n))
print("Sonni logarifmini hisoblash: ", math.log10(n))
print("Sonni sinusini hisoblash: ", math.sin(n))
print("Sonni kosinusini hisoblash: ", math.cos(n))