money = int(input("Pul miqdorini kiriting: "))

if money > 15:
  print("Mazza Cola ichdim")

if money >= 15:
  print("Cola ichdim")
else:
  print("Cola ichmadim")

if money >= 15:
  money-=15
  print("Cola ichdim")
else:
  print("Cola ichmadim")

print(money, "Pul qoldi")

number = int(input("Nechchini o'ylading: "))

if number == 5:
  print("Topding")
else:
  print("Xato")

if number != 5:
  print("Topa olmading")
else:
  print("Topding")

first_teacher = int(input("Daromadni kiriting: "))
second_teacher = int(input("Daromadni kiriting: "))
expense = int(input("Xarajatni kiriting: "))

if (first_teacher + second_teacher) >= expense:
  print("Tabriklaymiz! Siz ishga qabul qilindingiz")
else:
  print("Uzur, Siz ishga qabul qilinmadingiz", "Salomat bo'ling")

a = 0
password = int(input("Parolni kiriting: "))

if password == 1234:
  a = 15

print(a)

money = int(input( "Pul miqdorini kiriting: "))

if money >= 15:
  money-=15
  print("Cola ichdim")
  if money <= 5:
    money += 3
    print("Sizga keshbek berildi!")
  else:
    print("Sizga keshbek berilmadi!")
else:
  print("Cola ichmadim")

print("Salomat bo'ling! Haridiniz uchun rahmat!")

x = int(input("X ni kiriting: "))
y = int(input("Y ni kiriting: "))

if x > y:
  print(x, "katta")
elif x < y:
  print(y, "katta")
else:
  print("Ular teng")

salary = int(input("Oylik maosh miqdorini kiriting: "))

if salary <= 1000:
  tax = (salary * 10) / 100
elif salary <= 5000:
  tax = (salary * 20) / 100
else:
  tax = (salary * 30) / 100

print("Sizning solig'ingiz: ", tax)
print("Sizning sof oyligingiz: ", salary - tax)

year = int(input("Yilni kiriting: "))
cost = int(input("Narxni kiriting: "))

if year >= 2015:
  if cost <= 10000:
    print("Mashinani olaman!")
  else:
    print("Mashinani olmayman narxi qimmat ekan!")
else:
  print("Mashinani olmayman, yili eski ekan!")

year = int(input("Yilni kiriting: "))
cost = int(input("Narxni kiriting: "))

if year >= 2015 and cost <= 10000:
  print("Mashinani olaman!")
else:
  print("Mashinani olmayman, yili eski ekan!")

year = int(input("Yilni kiriting: "))
cost = int(input("Narxni kiriting: "))

if year >= 2015 or cost <= 10000:
  print("Mashinani olaman!")
else:
  print("Mashinani olmayman, yili eski ekan!")

year = int(input("Yilni kiriting: "))

if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
  print("Kabisa yili")
else:
  print("Kabisa yili emas")