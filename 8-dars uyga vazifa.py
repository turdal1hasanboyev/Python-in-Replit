# 1-vazifa

count = 10

while  count > 0:
    print(count)
    count -= 1
    if count == 0:
      print("Vaqt tugadi!")

# 2-vazifa

work = True

while work == True:
  answer = int(input("Ishlashni davom ettirasizmi? 1/0: "))
  if answer == 0:
    work = False
    print("Ilova yopilmoqda!")

# 3-vazifa

password = int(input("Parolni kiriting: "))

while  password != "0550":
  print("Kompyuter bloklangan. Skeytni qaytarib bersang = blokdan yechish kodini aytaman!")
  password = input("Parolni kiriting: ")

print("Kod to'g'ri, ishni yakunlayman…")

# 4-vazifa

a = int(input("'Men dasturchiman' iborasi necha martta chiqarilsin? "))

while a > 0:
  print("Men dasturchiman!")
  a -= 1

# 5-vazifa

a = int(input("Necha martta yodga solish kerak? "))

while a > 0:
  print("Siz nimanidir yoddan chiqarmaslikni istarmidingiz")
  a -= 1

# 6-vazifa

num_bag = int(input("Qoplar sonini kiriting: "))
summ = 0
count = 0

while  num_bag > count:
  print(count + 1, "- Qopni kiriting: ")
  bag = int(input("Qop og'irligini kiriting: "))
  summ += bag
  count += 1

print("Jami qoplar og'irligi: ", summ)