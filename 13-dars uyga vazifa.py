# 1-vazifa

for i in range(1, 10):
  for j in range(1, 10):
    print(i * j, end = " ")
  print("\t")

# 2-vazifa

n = int(input("Raqamni kiriting: "))

for row in range(n+1):
  for col in range(n+1):
    print(row + col, end = " ")
  print()

# 3-vazifa

for row in range(0, 10):
  for col in range(0, -10, -1):
    print(row + col, end = " ")
  print("\t")

# 4-vazifa

n = int(input("Qatorni kiriting: "))
n_1 = int(input("Ustunni kiriting: "))

for row in range(1, n+1):
  for col in range(1, n_1+1):
    if row % 2 == 0:
      print(row, end = " ")
    else:
      print(col, end = " ")
  print()

# 5-vazifa

m = int(input("Matritsa o'lchamini kiriting: "))

for row in range(1, m+1):
  for col in range(1, m+1):
    if col % 3 == 0:
      print(col, end = " ")
    else:
      print(row, end = " ")
  print()

# 6-vazifa

for row in range(20):
  for col in range(50):
    if row == 10:
      print('-', end = '')
    elif col == 25:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

# 7-vazifa

for row in range(20):
  for col in range(30):
    if row == 0:
      print('-', end = '')
    elif col == 0 or col == 29:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

# 8-vazifa

for row in range(20):
  for col in range(50):
    if row == 10:
      print('-', end = '')
    elif col == 25:
      print('|', end = '')
    elif col + row == 21:
      print('/', end = '')
    elif col - row == 29:
      print('\\', end = '')
    else:
      print(' ', end = '')
  print()

# 9-vazifa

m = int(input("Matritsa o'lchamini kiriting: "))

for row in range(m):
  for col in range(m):
    if row == col:
        print("1", end=" ")
    elif row < col:
        print("2", end=" ")
    else:
        print("0", end=" ")
  print()

# 1-vazifa

n = int(input("Raqamni kiriting: "))
counter = 1

for i in range(n, 0, -1):
  print(counter, "- soat")
  for j in range(i):
      print(j + (counter-1), "navbat")
  counter += 1
  print()

# 2-vazifa

summ = 0
n = int(input("Nechta son kiritasiz: "))

for num in range(n):
  number = int(input("Sonni kiriting: "))
  while  number > 0:
    if number % 10 > 5:
      summ += 1
    number //= 10

print(summ)

# 3-vazifa

m = int(input("Matritsa o'lchamini kiriting: "))

for row in range(1, m+1):
  for col in range(row-1, m+1):
    print(col, end = ' ')
  print()