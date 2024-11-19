# 1 - masala

x = int(input("X ni kiriting: "))
y = int(input("Y ni kiriting: "))

if x > y:
    print(x, "katta", y, "kichikroq")

if x < y:
    print(x, "kichikroq", y, "katta")
else:
    print("Ular teng")

# 2 - masala

balance = int(input("Balansni kiriting: "))

if balance > 75000:
    balance -= 75000
    print("Kurs muvafaqqiyatli harid qilindi")
    if balance < 5000:
        balance += 1000
        print("Chegirma qilindi!")
    else:
        print("Chegirma qilinmadi!")
    print("Balans: ", balance)
else:
  print("Kurs muvaffaqiyatli harid qilinmadi!")

print("Xayrli kun!")

# 3 - masala

money = int(input("Pul miqdorini kiriting: "))

if money >= 60:
  money -= 60
  print("Pishloqqa pul yetti")
  if money >= 20:
    money -= 20
    print("Muzqaymoqqa ham yetti")
  else:
    print("Muzqaymoqqa pul kam")

# 4 - masala

x = int(input("X ni kiriting: "))
y = int(input("Y ni kiriting: "))

if x > y:
   print(x, "katta",  y, "kichik")
elif x < y:
    print(x, "kichik", y, "katta")
else:
    print("Ular teng")

# 5 - masala

salary = int(input("Oylik maoshingizni kiriting: "))

if salary < 0:
  tax = 0
  print("Xato!, maoshingiz manfiy bo'lmasligi kerak")
elif salary < 10000:
  tax = (salary * 13) / 100
elif salary < 50000:
  tax = (salary * 20) / 100
else:
  tax = (salary * 30) / 100

print("Sizning solig'ingiz: ", tax)
print("Sizning sof maoshingiz: ", salary - tax)

# 6 - masala

coin1 = int(input("Birinchi tanga og'irligini kiriting: "))
coin2 = int(input("Ikkinchi tanga og'irligini kiriting: "))
coin3 = int(input("Uchinchi tanga og'irligini kiriting: "))

if coin1 == coin2:
  print("Uchinchi tanga yengil ya'ni qalbaki")
elif coin1 == coin3:
    print("Ikkinchi tanga yengil ya'ni qalbaki")
else:
  print("Birinchi tanga yengil ya'ni qalbaki")