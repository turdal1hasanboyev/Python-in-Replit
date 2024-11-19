# 1-vazifa

def summ_n():
  summ = 0

  for num in range(1, number + 1):
    summ += num

  print("1 dan", number, "gacha bo'lgan raqamlar yig'indisi", summ, "ga teng.")

number = int(input("Raqamni kiriting: "))

summ_n()

# 2-vazifa

def positive():
  print("Musbat")

def negative():
  print("Manfiy")

def test():
  son = int(input("Butun son kiriting: "))

  if son > 0:
      positive()
  elif son < 0:
      negative()
  else:
      print("Nolga teng")

test()

# 3-vazifa

def raqamlar_yigindisi(sonlar):
  summ = 0

  while  sonlar > 0:
    summ += sonlar % 10
    sonlar //= 10

  print("Raqamlar yig'indisi: ", summ)

def maksimal_raqam(sonlar):
  max_raqam = 0

  while  sonlar > 0:
    if sonlar % 10 > max_raqam:
      max_raqam = sonlar % 10
    sonlar //= 10

  print("Maksimal raqam: ", max_raqam)

def minimal_raqam(sonlar):
  min_num = 0

  while sonlar > 0:
    if sonlar % 10 < min_num:
      min_num = sonlar % 10
    sonlar //= 10

  print("Minimal raqam: ", min_num)

def kalkulyator():
  while True:
    print("1 - Raqamlar yig'indisini hisoblash")
    print("2 - Maksimal raqamni topish")
    print("3 - Minimal raqamni topish")
    print("0 - Chiqish")

    tanlov = input("Tanlovni tanlang: ")

    if tanlov == "0":
      break
    elif tanlov == "1":
      sonlar = int(input("Sonni kiriting: "))
      raqamlar_yigindisi(sonlar)
    elif tanlov == "2":
      sonlar = int(input("Sonni kiriting: "))
      maksimal_raqam(sonlar)
    elif tanlov == "3":
      sonlar = int(input("Sonni kiriting: "))
      minimal_raqam(sonlar)

kalkulyator()

# 4-vazifa

def raqamni_teskari_chiqarish(raqam):
  teskari_raqam = 0

  while raqam > 0:
    teskari_raqam = teskari_raqam * 10 + raqam % 10
    raqam //= 10

  print("Teskari raqam: ", teskari_raqam)

while  True:
  num = int(input("Sonni kiriting: "))

  if num == 0:
    print("Dastur yakunlandi!")
    break

  raqamni_teskari_chiqarish(num)

# 5-vazifa

def count_letters(text, k, n):
  count_k = 0
  count_n = 0

  for symbol in text:
    if symbol == k:
      count_k += 1
    elif symbol == n:
      count_n += 1

  print("Kiritilgan harflar soni: ", count_k)
  print("Kiritilgan sonlar soni: ", count_n)

text = input("Matn kiriting: ")
k = input("Kiritilgan harf: ")
n = input("Kiritilgan son: ")

count_letters(text, k, n)

# 6-vazifa

def tekshir_kvadratga_tegishlik(x, y):
  x_chegara = 5
  y_chegara = 5

  if (0 <= x <= x_chegara) and (0 <= y <= y_chegara):
      print("Tangacha shu yaqinda")
  else:
      print("Ushbu joyda tangacha yo'q")

x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

tekshir_kvadratga_tegishlik(x, y)

# 7-vazifa

import math

def minimal_raqam(x, y):
  min_raqam = (x + y - abs(x - y)) / 2

  print("Eng kichik raqam: ", min_raqam)

x = int(input("x ni kiriting: "))
y = int(input("y ni kiriting: "))

minimal_raqam(x, y)

# 8-vazifa

def ekub(a, b):
  while a != 0 and b != 0:
    if a > b:
      a = a % b
    else:
      b = b % a

  print("EKUB: ", a + b)

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

ekub(a, b)

# 9-vazifa

def rock_paper_scissors():
  while True:
    print("1 - qaychi, 2 - qog'oz, 3 - tosh")
    son = int(input("Sonni kiriting: "))
    if son == 1:
      print("Siz 2-o'rinsiz!")
    elif son == 2:
      print("Siz yutqazdingiz!")
      break
    elif son == 3:
      print("Siz yutdingiz!")

def guess_the_number():
  while True:
    son = int(input("Sonni kiriting: "))
    if son == 5:
      print("Siz topdingiz")
      break

def mainMenu():
  while True:
    print("1 - Tosh qaychi qog'oz, 2 - Sonni topish, 3 - Dasturdan chiqish")
    son = int(input("Tanlang: "))
    if son == 1:
      rock_paper_scissors()
    elif son == 2:
      guess_the_number()
    elif son == 3:
      print("Dastur yakunlandi")
      break

mainMenu()