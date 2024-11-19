password  = int(input("Parolni kiriting: "))

while  password != 1234:
    print("Parol xato")
    password = int(input("Parolni qaytadan kiriting: "))

print("Parol to'g'ri")

salary = int(input("Balansni kiriting: "))

while  salary > 10000:
    product = int(input("Mahsulot narxini kiriting: "))
    salary -= product

print("Hisobni to'ldiring!")

number = int(input( "Sonni kiriting: "))
summ = 0

while number > 0:
    if number % 10 == 5:
        break
    summ += number % 10
    number //= 10

print("Yig'indi: ", summ)

a = 0

while a < 25 :
  a += 1
  print(a)

if a % 5 == 0:
  print("Hello World")

a = True

while  True:
  print(a)

is_raining = False
answer = int(input("1 yoki 0 ni kiriting: "))

if answer == 1:
    is_raining = True

if is_raining:
  print("Soyabonni ol")
else:
  print("Quyosh")

num = 0

while  num <=10:
  print(num)
  if num > 5:
    break
  num += 1

num_box = int(input("Qutilar sonini kiriting: "))
summ = 0
counter = 0

while  num_box > counter:
  print(counter+1, "Qopni kiriting: ")
  box = int(input("Qopni kiriting: "))
  summ += box

counter += 1

print("Jami: ", summ)

number = 10

while  number > 0:
  number -= 1
  if number == 5:
    continue
  print(number)