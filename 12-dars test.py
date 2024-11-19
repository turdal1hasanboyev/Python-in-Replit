# 1-vazifa

week = input("Hafta kunini kiriting: ")

while  True:
  if week == "Dushanba":
    print("Hafta kuni raqami: 1")
  elif week == "Seshanba":
    print("Hafta kuni raqami: 2")
  elif week == "Chorshanba":
    print("Hafta kuni raqami: 3")
  elif week == "Payshanba":
    print("Hafta kuni raqami: 4")
  elif week == "Juma":
    print("Hafta kuni raqami: 5")
  elif week == "Shanba":
    print("Hafta kuni raqami: 6")
  elif week == "Yakshanba":
    print("Hafta kuni raqami: 7")
  else:
    print("Bunday hafta kuni mavjud emas")
  week = input("Hafta kunini kiriting: ")

# 2-vazifa

summ = 0

for num in range(10):
  text = input("So'zni kiriting: ")
  if text == "Karamba":
    summ += 1

print("Kiritilgan so'zlarning", summ, "tasi mos keladi")

# 3-vazifa

summ = 0
text = input("So'zni kiriting: ")

for symbol in text:
  if symbol != "*":
    summ += 1
  elif symbol == "*":
    summ += 1
    break

print("'*' belgisi ", summ, "pozitsiyada joylashgan")

# 4-vazifa

series = int(input("Qatorlar sonini kiriting: "))
seat = int(input("Qatordagi o'rindiqlar sonini kiriting: "))
m = int(input("Qatorlar orasidagi bo'sh metrlar masofasini kiriting: "))

for num in range(series):
  print("=" * seat, "*" * m, "=" * seat)

# 5-vazifa

x = 8
y = 10

while  True:
  operator = input("Marsoxod (W/A/S/D): ")
  if operator == "W":
    if y < 20:
      y += 1
  elif operator == "S":
    if y > 0:
      y -= 1
  elif operator == "A":
    if x > 0:
      x -= 1
  elif operator == "D":
    if x < 15:
      x += 1
  print("Marsoxod", x, y, "pozitsiyasida joylashgan")
  operator = input("Marsoxod (W/A/S/D): ")

# 6-vazifa

max_n = 0
count = 0
text = input("Qatorni kiriting: ")

for symbol in text:
  if symbol == "s":
    count += 1
  else:
    if max_n < count:
      max_n = count
    count = 0

print("Eng uzun ketma-ketlik: ", max_n)

# 7-vazifa

max_n = 0
count = 0
text = input("Matnni kiriting: ")

for symbol in text:
  if symbol != " ":
    count += 1
  else:
    if max_n < count:
      max_n = count
    count = 0

print("Eng uzun so'z: ", max_n)

# 8-vazifa

title = int(input("Konstitulning umumiy sonini kiriting: "))
exclamation = int(input("Undov belgisi sonini kiriting: "))

print("~" * (title // 2), "!" * exclamation, "~" * (title // 2))

# 9-vazifa

l = 2
summ = 0

for n in range(1, 11):
  band = input("Molxonada sigir bormi? ")
  if band == "b":
    summ += l
  l += 2

print("Bir kunlik sut miqdori: ", summ, "litr")

# 10-vazifa

text = input("Shifrlangan xabarni kiriting: ")
new_text = ""
new_text_2 = ""
count = 0

for symbol in text:
  count += 1
  if count % 2 != 0:
    new_text += symbol
  else:
    new_text_2 = symbol + new_text_2

print("Shifrsizlangan xabar", new_text + new_text_2)