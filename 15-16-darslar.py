def main():
  order = int(input("Buyruqni kiriting: 1-yaxshi, 0-yomon: "))

  if order == 1:
    good()
  elif order == 0:
    bad()
  else:
    print("Buyruq noto'g'ri kiritildi")
    main()

def good():
  print("Yaxshi")

  n = int(input("Davom etish uchun biron raqamni bosing: "))

  main()

def bad():
  print("Yomon")

  n = int(input("Davom etish uchun biron raqamni bosing: "))

  main()

main()

def reg_fruit():
  veg = int(input("Qancha sabzavod berildi?: "))
  fruits = int(input("Qancha meva berildi?: "))

print("Fil")

reg_fruit()

print("Jirafa")

reg_fruit()

print("Maymun")

reg_fruit()

print("Mushuk")

reg_fruit()

def main():
  order = int(input("Buyruqni kiriting: 1-uchburchak, 2-tog'ri to'rtburchak: "))

  if order == 1:
    triangle()
    main()
  elif order == 2:
    rectangle()
    main()
  else:
    print("Buyruq noto'g'ri kiritildi")
    main()

def triangle():
  a = int(input("Uchburchakning birinchi tomoni: "))
  b = int(input("Uchburchakning ikkinchi tomoni: "))

  print("Uchburchakning yuzi: ", (a * b) / 2)

def rectangle():
  a = int(input("Tog'ri to'rtburchakning birinchi tomoni: "))
  b = int(input("Tog'ri to'rtburchakning ikkinchi tomoni: "))

  print("Tog'ri to'rtburchakning yuzi: ", a * b)

main()

def adress(name):
  print("Ismi: ", name)
  print("Familiyasi: Hasanboyev")
  print("Mahalla: Hamza MFY")
  print("Uy: Yaxshi niyat ko'chasi 7-uy")

  name = input("Ismingizni kiriting: ")

  adress(name)

name = input("Ismingizni kiriting: ")

adress(name)

def adress(name, num):
  print("Ismi: ", name)
  print("Familiyasi: Hasanboyev")
  print("Mahalla: Hamza MFY")
  print("Uy: Yaxshi niyat ko'chasi"+num+"-uy")

  name = input("Ismingizni kiriting: ")
  num = int(input("Uyning raqamini kiriting: "))

  adress(name, num)

name = input("Ismingizni kiriting: ")
num = int(input("Uyning raqamini kiriting: "))

adress(name,num)

import math

def distance(x, x1, y, y1):
  dis = math.sqrt(((x - x1) ** 2) + ((y - y1) ** 2))

  print("Masofa: ", round(dis))

x = int(input("X ni kiriting: "))
x1 = int(input("X1 ni kiriting: "))
y = int(input("Y ni kiriting: "))
y1 = int(input("Y1 ni kiriting: "))

distance(x, x1, y, y1)

def cal_tax(price,tax):
  total = price + (price * tax / 100)
  return total

price = float(input("Maxsulot narhini kiriting: "))
tax = int(input("Maxsulot solig'ini kiriting: "))
total = cal_tax(price, tax)

print(total)

count = 0
x = 1

while x != 0:
  x /= 2
  count += 1

print(count)

a = 1.769
b = 1769 * 10 ** -3
c = 1769e-3

print(a, b, c)

a = 2.400
b = 2400 * 10 ** -3
c = 2400e-3

print(a, b, c)

a = 1.1 + 2.2

print(a)

a = 1.1 + 2.2

print(round(a, 1))

a = 1.1
b = 2.2
c = a + b
d = 3.3

if abs(c - d) < 1e-15:
  print("To'g'ri")
else:
  print("Noto'g'ri")