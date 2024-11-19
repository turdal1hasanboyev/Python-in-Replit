# 1-vazifa

number = int(input("Raqamni kiriting: "))
summ = 0

while  number > 0:
  summ += number
  number = int(input("Raqamni kiriting: "))

print(summ)

# 2-vazifa

password = int(input("Parolni kiriting: "))

while password != 235:
  print("Notog'ri parol!")
  password = int(input("Yana bir bor urinib ko'ring: "))

print("Tog'ri parol! Xush kelibsiz.")

# 3-vazifa

save = int(input("Qancha pul tejab qo'yish kerak? "))
foundation = 0
foundation += save

while foundation < 500000:
  save = int(input("Qancha pul tejab qo'yish kerak? "))
  foundation += save

print("Tejab qo'yildi!")

# 4-vazifa

temperature = int(input("Haroratni kiriting: "))
s = 0

while temperature > 15:
  s += 20
  temperature -= 2
  if temperature <= 15:
    break
  s += 10

print("Sportchi bosib o'tgan masofa: ", s, "ga teng")

# 5-vazifa

n = int(input("Raqamni kiriting: "))
summ = 0

while  n % 10 != 5:
  summ += n % 10
  n = n // 10

print(summ)

# 6-vazifa

summ = int(input("Boshlang'ich pul miqdorini kiriting: "))

while  summ < 10000:
  cube = int(input("Kubikda qanday son hosil bo'ldi? "))
  if cube != 3:
    print("500 rublni yutib oldingiz!")
    summ += 500
  if summ >= 10000:
    print("O'yin yakunlandi")
    print("Sizda qolgan pul miqdori: ", summ)
    break
  if cube == 3:
    print("Siz hammasini yutqazdingiz!")
    summ = 0
    print("Sizda qolgan pul miqdori", summ, "rubl")
    print("O'yin yakunlandi!")
    break
  cube = int(input("Kubikda qanday son hosil bo'ldi? "))