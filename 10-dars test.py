# 1-vazifa

for num in 114, 12, 14, 10605, 4709, 450:
  if num % 2 == 0 and num % 3 == 0:
    print(num, "Raqam mos")
  else:
    print(num, "Raqam mos emas")

# 2-vazifa

summ = 0

for num in range(1, 11):
  print(num, "- raqamni kiriting")
  n = int(input())
  if n > 0 and n % 2 == 0:
    summ += 1

print(summ, "ta musbat va juft son kiritildi")

# 3-vazifa

summ = 0

for mounth in range(1, 13):
  print(mounth, "- oy uchun ish haqqini kiriting")
  money = int(input())
  summ += money

print("O'rtacha yillik ish haqi: ", summ, "ga teng")

# 4-vazifa

violation = 0

for n in range(30, 36):
  print(n," - sektordagi odamlar sonini kiriting: ")
  people = int(input())
  if people > 10:
    violation += 1
    print("Qoidabuzarlik! Sektordagi odamlar soni keragidan ko'p")
  else:
    print("Hammasi joyida!")

print("Qoida buzarliklar soni", violation, "ta")

# 5-vazifa

summ = 1

n = int(input("Raqamni kiriting: "))

for num in range(1, n+1):
  summ *= num

print(summ)

# 6-vazifa

alochi_oquvchilar = 0
yaxshi_oquvchilar = 0
uch_baholi_oquvchilar = 0

n = int(input("Sinfda nechta o'quvchi bor? "))

for people in range(1, n+1):
  print(people, "- O'quvchi necha baho oldi? ")
  ball = int(input())
  if ball == 5:
    alochi_oquvchilar += 1
  elif ball == 4:
    yaxshi_oquvchilar += 1
  elif ball == 3:
    uch_baholi_oquvchilar += 1

if alochi_oquvchilar > yaxshi_oquvchilar and alochi_oquvchilar > uch_baholi_oquvchilar:
  print("Sinfda a'lochi o'quvchilar ko'p!")
elif yaxshi_oquvchilar > alochi_oquvchilar and yaxshi_oquvchilar > uch_baholi_oquvchilar:
  print("Sinfda yaxshi o'quvchilar ko'p!")
else:
  print("Sinfda uch baholi o'quvchilar ko'p!")

# 7-vazifa

summ = 0

a = int(input("Raqamni kiriting: "))
b = int(input("Raqamni kiriting: "))

for num in range(a, b):
  if num % 3 == 0:
    summ += num

print(summ / (b-a))

# 8-vazifa

for num in range(1, 100):
  if num * 3 < 100 and num * 3 > 10:
    print(num * 3)

# 9-vazifa

salary = 0
counter = 0

for n in range(1, 11):
  print(n, "- oylikni kiriting")
  num = int(input())
  salary = num + salary
  if salary <= num:
    counter += 1

if counter == 10:
  print("Oylik o'suvchi")
elif counter == 0:
  print("Oylik kamayuvchi")
else:
  print("Oylik o'suvchi ham kamayuvchi ham emas")

# 10-vazifa

summ = 0

n = int(input("Kartalar sonini kiriting: "))

for num in range(1, n+1):
  summ += num

for num in range(1, n):
  card = int(input("Qolgan karta raqamini kiriting: "))
  summ -= card

print("Yo'qolgan karta raqami ", summ)