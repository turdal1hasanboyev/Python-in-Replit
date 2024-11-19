# 1 - 6 talik topshiriq

# 1-vazifa

ball = 0

for num in range(5):
  book = input("Asarni kim yozgan? ")
  if book == "Yevgeniy Onegin":
    print("To'g'ri!")
    break
  else:
    print("Noto'g'ri!")
    ball += 1

print("Sinfda 2 baho olgan o'quvchilar soni: ", ball, "ta")

# 2-vazifa

work = True

while work == True:
  working = input("Kecha bergan vazifamni bajardingmi? ")
  if working == "Ha, albatta bajardim!":
    work = False

# 3-vazifa

name = input("Ismingiz nima? ")
name_1 = "Fil sotib oling!"
name_2 = "Yaxshi, sotib olaman!"

print("Sotuvchi", name, name_1)
print("Men", name_2)

nam = True

while nam == True:
  print("Hamma", name_2)
  print("Men", name_1)

# 4-vazifa

for symbol in "Python!":
  print("\n", symbol)

# 5-vazifa

text = input("So'zni kiriting: ")

for symbol in text:
  print(symbol * 3, end="")

# 6-vazifa

text = input("So'zni kiriting: ")
y_1 = 0
y_2 = 0

for symbol in text:
  if symbol == 'A':
    y_1 += 1
  elif symbol == 'a':
    y_2 += 1

print("Katta A harflar soni", y_1, "Kichik a harflar soni", y_2)

# 2- 3 talik topshiriq

# 1-vazifa

for n in range(5):
  print("||-=-=-=-=-=-=-=-=||")
  print("||                ||")
  print("||                ||")
  print("||     Vector     ||")
  print("||                ||")
  print("||                ||")
  print("||-=-=-=-=-=-=-=-=||")

# 2-vazifa

a1 = int(input("Birinchi sonni kiriting: "))
d = int(input("Oraliq masofani kiriting: "))
summ = 0

for num in range(3):
  print(a1, end = '.')
  summ += a1
  a1 += d

print(summ)

# 3-vazifa

n = int(input("Sonni kiriting: "))

for num in range(0, n+1, 10):
  print(num, end = '-=-')