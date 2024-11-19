# 1 - 6 talik topshiriq

# 1-vazifa

n = int(input("Sonni kiriting: "))

for num in range(2, n + 1, 2):
  print(num ** 3)

# 2-vazifa

summ_cell = 0
cell = 1
time = int(input("Soatni kiriting: "))

for hour in range(3, time+1, 3):
  print("O'tgan soat: ", hour)
  cell *= 2
  print("Hujayralar soni: ", cell)
  summ_cell += cell
  print("Tajriba tugashigacha qolgan soat: ", time - hour)
  if hour == time:
    print("Tajriba tugadi")
    print("Hujayralar soni: ", summ_cell)

# 3-vazifa

n = int(input("Sonni kiriting: "))

for num in range(1, n + 1, 2):
  print(num ** 2)

# 4-vazifa

n = int(input("Sonni kiriting: "))

for num in range(1, n + 1, 2):
  print(num * 2)

# 5-vazifa

summ = 0
n = int(input("Stul raqamini kiriting: "))

for num in range(1, n + 1, 5):
  summ += num

print("Stullar raqamlar yig'indisi: ", summ, "ga teng")

# 6-vazifa

summ_cal = 0
summ_water = 0
vake_up = int(input("Nechchida uyg'onding: "))

for hour in range(vake_up, 23, 3):
  summ_water += 1
  cal = int(input("Qancha kaloriya ovqat yeding: "))
  summ_cal += cal

print(summ_water, "litr suv va", summ_cal, "kaloriya istemol qilindi")

# 2 - 3 talik topshiriq

# 1-vazifa

time = int(input("Soniyalar sonini kiriting: "))

for second in range(time, 0, -1):
  print(second)

print("Men qidirishni boshladim!")

# 2-vazifa

summ = 0
num_sold = int(input("Askarlar soni: "))
num_order = int(input("Qonunlar sonini kiriting: "))

for soldier in range(num_sold-4, 0, -4):
  print(soldier, "- Askar qonunlar sonini ayt")
  order = int(input())
  if order == num_order:
    print("Yaxshi askar!")
  else:
    print("Yotib tortil")
    summ += (soldier * 10)

print("Barcha yotib tortilishlar soni: ", summ)

# 3-vazifa

n = int(input("Sonni kiriting: "))

if n % 2 == 0:
  for num in range(n, 0, -2):
    print(num)
else:
  for num in range(n-1, 0, -2):
    print(num)