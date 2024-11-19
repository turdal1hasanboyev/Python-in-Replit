# 1-vazifa

for num in range(1, 11):
  print(num ** 3)

# 2-vazifa

summ = 0
num_1 = int(input("1 - sonni kiriting: "))
num_2 = int(input("2 - sonni kiriting: "))

for number in range(num_1, num_2 + 1):
  summ += number

print(num_1, "dan", num_2, "gacha bo'lgan sonlar yig'indisi", summ, "ga teng")

# 3-vazifa

summ = 0
vake = int(input("Soat nechida uyg'onding: "))

for hour in range(vake, 23):
  print(hour, "- soatda necha kaloriya ovqat yeding: ")
  cal = int(input())
  summ += cal
  if summ >= 2000:
    print("Yetarlicha ovqat yeding uhla!")
    break