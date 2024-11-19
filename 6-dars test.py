# 1-masala

# 1000 tajriba ochkolar tizimi uchun

n = int(input("Tajriba ochkolari sonini kiriting: "))

if n % 1000 == 0:
  print("Sizning bosqichingiz", n // 1000)

# 2500 tajriba ochkolar tizimi uchun

n = int(input("Tajriba ochkolari sonini kiriting: "))

if n % 2500 == 0:
  print("Sizning bosqichingiz", n // 2500)

# 5000 tajriba ochkolar tizimi uchun

n = int(input("Tajriba ochkolari sonini kiriting: "))

if n % 5000 == 0:
  print("Sizning bosqichingiz", n // 5000)

# 2-masala

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

if a > b and a > c:
  print("Birinchi son katta", "ya'ni", a)
elif b > a and b > c:
  print("Ikkinchi son katta", "ya'ni", b)
elif c > a and c > b:
  print("Uchinchi son katta", "ya'ni", c)

# 3-masala

x = int(input("Iksni kiriting: "))

if x == 0:
  print("Igrek", 5, "ga teng")
else:
  print("Igrek", x ** 2, "ga teng")

# 4-masala

n = int(input("O'qishga kirayotganlar ro'yxatidagi o'rinni kiriting: "))
ball = int(input("Imtihonlarda olgan ballar sonini kiriting: "))

if n < 10:
  print("Tabriklaymiz, Siz o'qishga kirdingiz!")
  if ball >= 290:
    print("Bonus sifatida sizga stipendiya hisoblab beriladi!")
  else:
    print("Tabriklaymiz, Siz o'qishga kirdingiz!")
    print("Lekin stipendiya olish uchun sizda ballar yetishmadi!")

# 5-masala

rating = int(input("Matematikadan nechchi baho olding? "))

if rating == 2 or rating == 3:
  print("Yomon. Jo'na, tayyorlan!")
elif rating == 4 or rating == 5:
  print("Balli! Dam olishing mumkin.")

# 6-masala

n = int(input("Sonni kiriting: "))

if n < -9 and n > -100:
  print("Siz kiritgan son 2 xonali son!")
else:
  print("Siz kiritgan son 2 xonali son emas!")

# 7-masala

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

if a == b == c:
  print(3)
elif a == b or a == c or b == c:
  print(2)
else:
  print(0)

# 8-masala

home_price = int(input("Honadon narxini kiriting: "))
home_square = int(input("Honadon yuza kvadratini kiriting: "))

if home_price < 10000000 and home_square > 100:
  print("Honadon to'gri keladi!")
elif home_price < 7000000 and home_square > 80:
  print("Honadon to'gri keladi!")
else:
  print("Honadon to'g'ri kelmaydi!")

# 9-masala

salary = int(input("Oylik maoshingizni kiriting: "))

if salary < 0 or salary == 0:
  tax = 0
  print("Oylik maosh 0 ga teng bo'lishi yoki manfiy bo'lishi mumkin emas")
elif salary > 0 and salary <= 10000:
  tax = (13 / 100) * salary
elif salary > 10000 and salary <= 50000:
  tax = (20 / 100) * (salary - 10000) + (13 / 100) * (10000)
else:
  tax = (30 / 100) * (salary - 50000) + (20 / 100) * (50000 - 10000) + (13 / 100) * (10000)

print("Sining solig'ingiz: ", tax)
print("Sizning sof oylik maoshingiz: ", salary - tax)

# 10-masala

# 1-usul

clock = int(input("Vaqtni kiriting: "))

if (clock > 8 and clock < 22) or (clock < 13 and clock > 16) or (clock < 9 and clock > 13) or (clock < 17 and clock > 21):
  print("Jo'natmani olish mumkin!")
else:
  print("Jo'natmani olish mumkin emas!")

# 2-usul

clock = int(input("Vaqtni kiriting: "))

if (clock < 8 or clock > 22) or (clock > 13 or clock < 16) or (clock > 9 or clock < 13) or (clock > 17 or clock < 21):
  print("Jo'natmani olish mumkin emas!")
else:
  print("Jo'natmani olish mumkin!")