# 1-vazifa

for i in range(6):
  for j in range(0, 11, 2):
    print(i+j, end = '\t')
  print()

# 2-vazifa

n = int(input("Raqamni kiriting: "))

for row in range(1, n+1):
  for col in range(row):
    print(row, end = '\t')
  print()

# 3-vazifa

a = int(input("Balandlikni kiriting: "))
b = int(input("Enini kiriting: "))

for row in range(a):
  for col in range(b):
    if row == 0 or row == a-1:
      print('-', end = '')
    elif col == 0 or col == b-1:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

# 4-vazifa

for row in range(20):
  for col in range(20):
    if row == col or row + col == 20 - 1:
        print("^", end=" ")
    else:
        print(" ", end=" ")
  print()

# 5-vazifa

summ = 0
num_num = int(input("Nechta son kiritasiz?: "))

for i in range(num_num):
  new_num = int(input("Raqamni kiriting: "))
  while new_num > 0:
    if (new_num % 10) % 2 == 0:
      summ += 1
    new_num //= 10

print("Ketma-ketlikda oddiy raqamlar soni: ", summ)

# 6-vazifa

summ = 1
summ_2 = 0
n = int(input("Sonni kiriting: "))

for i in range(1, n+1):
  summ *= i
  summ_2 += summ

print("Faktoriallar yig'indisi: ", summ_2, "ga teng")

# 7-vazifa

max_num = 0
max = 0
summ = 0
n = int(input("Nechta sonni kiriting: "))

for i in range(n):
  new_num = int(input("Sonni kiriting: "))
  if new_num > max_num:
    max_num = new_num
  while  new_num > 0:
    summ += (new_num % 10)
    new_num //= 10
  if summ > max:
    max = summ
  summ = 0

print("Kiritilgan sonlar ichida eng katta raqamlar yig'indisi: ", max, "Va eng katta son: ", max_num)

# 8-vazifa

h = int(input("Peramidaning balandligini kiriting: "))

for i in range(1, h+1):
  print(" " * (h - i) + "#" * (i * 2-1))