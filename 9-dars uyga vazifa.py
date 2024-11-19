# 1-vazifa

for meters in 100, 90, 95, 87, 102:
 if meters % 3 == 0:
   print(meters, 'Mos keladi')
 else:
   print(meters, 'Mos kelmaydi')

# 2-vazifa

for number in 3, 7, 5, 6, 4:
  print(number ** 2, number ** 3, number ** 4)

# 3-vazifa

win = 0

for ticket in 345, 19, 87, 1020, 421:
  if (ticket > 99 and ticket < 1000) and (ticket % 5 == 0):
    print(ticket, "chipta yutuqli!")
    win += 1
  else:
    print(ticket, "chipta yutuqli emas!")

print("G'oliblar soni:", win)

# 4-vazifa

for num in range(11):
  print(num ** 2)

# 5-vazifa

hour = int(input("Soat nechchi? "))

for hour in range(hour):
  print("Ku-Ku!")

# 6-vazifa

for num in range(21):
  print(2 ** num)