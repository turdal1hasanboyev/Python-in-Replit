# 1-vazifa

n = int(input("Sonni kiriting: "))
a = 1

while  a <= n:
  print(a ** 3)
  a += 1

# 2-vazifa

name = input("Ismingizni kiriting: ")

print(name+",Sizning qarzingiz 100 rublni tashkil qiladi.")

money = 0

while  money <= 100:
  money = int(input("Buni to'lash uchun qancha rubl kiritasiz? "))
  if money < 100:
    print("Bu kam", name+".Yana qo'shing.")
  if money >= 100:
    print("Juda yaxshi,", name+",Siz qarzingizni to'ladingiz. Rahmat!")
    break

# 3-vazifa

n = int(input("Sonni kiriting: "))
summ = 0

while n > 0:
  n % 10
  n = n // 10
  summ += 1

print(summ)

# 4-vazifa

day = 0
day_num = 0
mounth = int(input("Oylar sonini kiriting: "))

while  mounth > 0:
  day = (mounth * 30) // 2
  day_num += day
  mounth = int(input("Oylar sonini kiriting: "))

print("Juft kunlar soni: ", day_num)

# 5-vazifa

ticket = int(input("Chipta raqamini kiriting: "))

while  ticket > 0:
  if (ticket // 100000 % 10) + (ticket // 10000 % 10) + (ticket // 1000 % 10) == (ticket // 100 % 10 + ticket // 10 % 10 + ticket % 10):
    print("Bu chipta omadli")
  else:
    print("Bu chipta omadli emas")
  ticket = int(input("Chipta raqamini kiriting: "))

# 6-vazifa

n = int(input("Raqamni kiriting: "))
positive = 0
negative = 0

while  n != 0:
  if n > 0:
    positive += 1
  if n < 0:
    negative += 1
  n = int(input("Raqamni kiriting: "))

print("Musbat raqamlar soni: ", positive)
print("Manfiy raqamlar soni: ", negative)

# 7-vazifa

counter = 0
clock = 0
summ = 0

print("8-soatlik ish kuni boshlandi!")

while  clock < 8:
  clock += 1
  print(clock, "-soat")
  work = int(input("Turdiali nechta vazifani bajaradi? "))
  summ += work
  phone = int(input("Xotini qo'ng'iroq qilmoqda. Javob berish kerakmi? 1 ha 0 yo'q "))
  if phone == 1:
    counter += 1

print("Ish vaqti tugadi! Jami bajarilgan vazifalar soni: ", summ)

if counter > 0:
  print("Dokonga borish kerak!")

# 8-vazifa

year = 0

x = int(input("Bankga qancha omonat qo'ymoqchisiz: "))
p = int(input("Yillik foiz stavkani kiriting: "))
y = int(input("Omonatni qancha bo'lganda qaytarib olmoqchisiz? "))

while  x < y:
  x += int(x * (p / 100))
  year += 1

print("Omonatni", year, "yildan so'ng qaytarib olasiz")

# 9-vazifa

x = 7
num = 1
a = int(input("Sonni kiriting: "))

while  a != x:
  if a > x:
    print("Raqam kerak bo'lganidan katta. Yana bir bor urinib koring!")
  if a < x:
    print("Raqam kerak bo'lganidan kichkina. Yana bir bor urinib koring!")
  a = int(input("Sonni kiriting: "))
  num += 1

print("Siz topdingiz! " , "Urinishlar soni ", num)

# 10-vazifa

left_side = 0
right_side = 100
counter = 7

while  counter > 0:
  number = (left_side + right_side) // 2
  print(number, "ga 1 teng 2 katta 3 kichik")
  order = int(input())
  if order == 1:
    print("Son topildi!")
    break
  elif order == 2:
    left_side = number
  elif order == 3:
    right_side = number
  else:
    print("Xato buyruq kiritildi!")
  counter -= 1

print("Urinishlar tugadi!")