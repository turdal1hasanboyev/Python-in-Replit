for number in 17, 25, 141:
  print(number * 2)

for ticket in 20, 23, 25, 35, 55:
  if ticket % 5 == 0:
    print(ticket, "Yutuqli!")
  else:
    print(ticket, "Yutuqli emas!")

for num in range(11):
  print(num * 2)

summ = 0

for mounth in range(12):
  print(mounth + 1, "-oy")
  money = int(input("Pulni kiriting: "))
  summ += money

print("Yig'ilgan pul: ", summ, "ga teng")

for number in range(5, 36):
  print(number ** 2)

is_prime = False
number = int(input("Sonni kiriting: "))

for num in range(2, number // 2):
  if number % num == 0:
    print("Tub emas")
    is_prime = False
    break
  else:
    is_prime = True

if is_prime:
  print("Tub son")

range(1,10,2)

num = int(input("Sonni kiriting: "))

for number in range(1, num, 2):
  print(number ** 2)

summ_cal = 0
summ_water = 0
vake_up = int(input("Nechchida uyg'onding: "))

for hour in range(vake_up, 23, 3):
  cal = int(input("Qancha kaloriya ovqat yeding: "))
  summ_cal += cal

print(summ_cal)
print((23 - vake_up) // 2)

time = int(input("Vaqtni kiriting: "))

for sekund in range(time, -1, -1):
  print(sekund)

summ = 0
num_sold = int(input("Askarlar soni: "))
num_order = int(input("Qonunlar sonini kiriting: "))

for soldier in range(num_sold, 0, -2):
  print(soldier,"- Askar qonunlar sonini ayt")
  order = int(input())
  if order == num_order:
    print("Yaxshi askar!")
  else:
    print("Askar yotib tur!")
    summ += (soldier * 10)

print(summ)

for num_st in range(5):
  book = input("Xamsa asari muallifi kim? ")
  if book == "Alisher Navoiy":
    print("To'g'ri javob!")
    break
  else:
    print("No'to'g'ri javob!")

for symbol in 'Python':
  print(symbol)
  print(symbol, end = ',')

for symbol in 'Vector':
  print('\n', symbol)

a1 = int(input("Birinchi sonni kiriting: "))
d = int(input("Oraliq masofani kiriting: "))
summ = 0

for num in range(3):
  print(a1, end = '.')
  summ += a1
  a1 += d

print(summ)

text = input("Matnni kiriting: ")
new_text = ''

for symbol in text:
  if symbol != 1 or symbol != 9:
    new_text += symbol

print(new_text)

is_down = False
text = input("So'zni kiriting: ")
symbol_2 = ''

for symbol in text:
  if symbol == symbol_2:
    is_down = True
    symbol_2 = symbol

if is_down == True:
  print("So'zda ikkita xarf bor")
else:
  print("So'zda ikkita xarf yo'q")

for a in range(5):
  for b in range(5):
    print(a + b, end = ' ')
  print()

for a in range(1, 11):
  for b in range(1, 10):
    print(a, '*', b, '=', a * b)
  print()

for row in range(1, 6):
  for col in range(1, 6):
    if row % 2 == 0:
      print(row, end = '\t')
    else:
      print(col, end = '\t')
  print()

for row in range(30):
  for col in range(30):
    if row == 15:
      print('-', end = '')
    elif col == 15:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

for row in range(20):
  for col in range(50):
    if row == 10:
      print('-', end = '')
    elif col == 25:
      print('|', end = '')
    elif col + row == 19:
      print('/', end = '')
    elif col - row == 32:
      print('\\', end = '')
    else:
      print(' ', end = '')
  print()

a = int(input("Qatorlar sonini kiriting: "))
b = int(input("Ustunlar sonini kiriting: "))

for row in range(a):
  for col in range(b):
    if row == col:
      print(1, end = ' ')
    elif row > col:
      print(2, end = ' ')
    else:
      print(0, end = ' ')
  print()

counter = 1

for i in range(5, 0, -1):
  print(counter, "- soat")
  for j in range(i):
    print(j + counter, "navbat")
  counter += 1
  print()

print("Navabtda hechkim qolmadi")

num_num = int(input("Nechta son: "))
num = int(input("Qaysi raqam? "))
counter = 0

for i in range(num_num):
  new_num = int(input("Sonni kiriting: "))
  while new_num > 0:
    if new_num % 10 == num:
      counter += 1
    new_num //= 10

print(num_num, "ta sonda", counter, "ta", num, "raqami bor")

for i in range(3):
  password = int(input('Parolni kiriting: '))
  if password == 1234:
    print("Parol to'g'ri")
    break
else:
  print("Parol noto'g'ri")