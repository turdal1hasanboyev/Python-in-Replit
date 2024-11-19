# 1-vazifa

def greeting():
  print('Salom!')
  print('Xush kelibsiz!')

while True:
  a = input("Kirasizmi? Ha/Yo'q: ")
  if a == 'Ha':
    greeting()
  print('Keyingisi', end = '\n')

# 2-vazifa

def hisoblash_va_natijani_chiqarish(sorovnoma):
  print(sorovnoma)

  a = int(input())
  b = int(input())
  
  print("Jami", a + b, "dona")

hisoblash_va_natijani_chiqarish("Qancha qop baliq va go'sht bor?")
hisoblash_va_natijani_chiqarish("Qancha qora va oq non bor?")
hisoblash_va_natijani_chiqarish("Qancha chelak suv va sut bor?")

# 3-vazifa

def oila():
  print("Familiyasi: ", surname)
  print("Ismi: ", name)
  print("Ko'cha nomi: ", street)
  print("Uy raqami: ", house)
  print()

surname = "Yusupov"
name = "Bobur"
street = "Rustaveli"
house = "32"

oila()
oila()
oila()

# 1-vazifa

def water():
  print("Nomi: Clean Water")
  print("Ishlab chiqaruvchi: VodZavod")
  print("Narxi: ", price)

for i in range(3):
  price = int(input("Narxni kiriting: "))
  water()

# 2-vazifa

import math

def sphereArea():
  print("Sayyora yuzasi: ", 4 * math.pi * radius ** 2)

def sphereVolume():
  print("Sayyora hajmi: ", 4 / 3 * math.pi * radius ** 3)

radius = float(input("Sayyora radiusi kiriting: "))

sphereArea()
sphereVolume()

# 3-vazifa

def IsPrime():
  count = 0

  for i in range(1, number+1):
    if i % 2 != 0:
      count += 1
  print("Toq sonlar: ", count)

number = int(input("Raqamni kiriting: "))

IsPrime()

# 1-vazifa

def orta_arifmetik():
  summ = 0

  for i in range(a, b + 1):
    summ += i

  print("Orta arifmetik: ", summ / (b - a + 1))

a = int(input("Boshlang'ich raqamni kiriting: "))
b = int(input("Oxirgi raqamni kiriting: "))

if a < b:
  orta_arifmetik()
else:
  print("Xatolik: Boshlang'ich raqam oxirgi raqamdan kichkina bo'lishi kerak")

# 2-vazifa

def pochta_malumotlari(familiya, ism, mamlakat, shahar, kocha, uy_raqami, kvartira_raqami):
  print("Familiya:", familiya)
  print("Ism:", ism)
  print("Istiqomat qiluvchi mamlakat:", mamlakat)
  print("Shahar:", shahar)
  print("Ko'cha:", kocha)
  print("Uy raqami:", uy_raqami)
  print("Kvartira raqami:", kvartira_raqami)
  print()

pochta_malumotlari("Ismoilov", "Jamshid", "O'zbekiston", "Toshkent", "Mustaqillik", "12", "34")
pochta_malumotlari("Qodirov", "Abdulla", "Qozog'iston", "Almati", "Navoiy", "56", "78")
pochta_malumotlari("Nazarov", "Jamshid", "Rossiya", "Moskva", "Lenin", "90", "123")

# 3-vazifa

import math

def masofa(x1, y1, x2, y2):
  dis = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

  print("Masofa: ", dis)

def main(x,y):
  x_y = round(math.sqrt(x ** 2 + y ** 2), 2)

  print("X va Y orasidagi masofa: ", x_y)

tanlov = int(input("Tanlovni kiriting 1 yoki 2: "))

if tanlov == 1:
  x = float(input("Nuqta x koordinatini kiriting: "))
  y = float(input("Nuqta y koordinatini kiriting: "))
  main(x, y)
elif tanlov == 2:
  x1 = float(input("Birinchi nuqta x koordinatini kiriting: "))
  y1 = float(input("Birinchi nuqta y koordinatini kiriting: "))
  x2 = float(input("Ikkinchi nuqta x koordinatini kiriting: "))
  y2 = float(input("Ikkinchi nuqta y koordinatini kiriting: "))
  masofa(x1, y1, x2, y2)
else:
  print("Noto'g'ri tanlov!")