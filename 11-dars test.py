# 1-vazifa

buckwheat = 100

for mounth in range(1, buckwheat):
    print(mounth, " - oy")
    buckwheat -= 4
    print(buckwheat, "kg grechka qoldi")
    if buckwheat < 4:
        break

print("Grechka", mounth, "oyga yetadi")

# 2-vazifa

summ = 0
num_debtors = int(input("Qarzdorlar sonini kiriting: "))

for num_debtors in range(0, num_debtors + 1, 5):
    print(num_debtors, "- raqamli qarzdor")
    debt = int(input("Qarz qancha: "))
    summ += debt

print("Umumiy qarz miqdori: ", summ)

# 3-vazifa

second = int(input("Soniyani kiriting: "))

for n in range(second, -1 , -1):
    if n == 0:
        print("Bomba portladi!")
        break
    print("Bomba portlashiga", n, "soniya qoldi")
    bomb_of = int(input("Bombani faolsizlashtirishni hohlaysizmi: 1-ha 0-yo'q: "))
    if bomb_of == 1:
        print("Bomba portlashidan", n, "soniya oldin faolsizlantirildi!")
        break

# 4-vazifa

count = 0
summ = 0

a = int(input("Sonni kiriting: "))
b = int(input("Sonni kiriting: "))
c = int(input("Sonni kiriting: "))

for num in range(a, b+1):
  if num % c == 0:
    print(num)
    summ += num
    count += 1

print(summ / count)

# 5-vazifa

a = int(input("Kesimning boshini kiriting: "))
b = int(input("Kesimning oxirini kiriting: "))
x = int(input("Qadamni kiriting: "))

for n in range(b, a-1, x):
  y = (n * 3) + (2 * (n * 2)) - ((4 * n) + 1)
  print(n, "nuqtadagi funksiya qiymati: ", y, "ga teng")

# 6-vazifa

a = int(input("Xatning bo'yini kiriting: "))
b = int(input("Xatning enini kiriting: "))
n = 0

while  True:
  a /= 2
  b /= 2
  n += 1
  if a < 12 and b < 12:
    print("Xat", n, "martta buklanishi kerak")
    break

# 7-vazifa

summ = 0
educational_grant = int(input("Stipendiyani kiriting: "))
expences = int(input("Xarajatlarni kiriting: "))

for n in range(2, 11):
  summ += (expences / 100) * 3

print("Ota-onalaridan so'rashlari kerak: ", (expences * 10) + (summ) - (educational_grant * 10))

# 8-vazifa

summ = 0
s = int(input("Raqamni kiriting: "))
n = int(input("Sonni kiriting: "))

for num in range(1, n+1):
  s /= 2
  summ += s

print(summ)

# 9-vazifa

n = 1
summ = 1
x = int(input("X ni kiriting: "))

for n in range(1, 64):
  res = ( (x-n) ) / ((x - (n+1) ))
  summ *= res

print(summ)

# 10-vazifa

b = int(input("Og'il bolalar sonini kiriting: "))
g = int(input("Qiz bolalar sonini kiriting: "))

if b == g:
  for num in range((b+g) // 2):
    print("BG")
elif (g / b) > 2 or (b / g) > 2:
  print("Yechim yo'q")