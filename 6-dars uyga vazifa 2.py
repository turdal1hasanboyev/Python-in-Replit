# 1-masala

year = int(input("Velosiped yilini kiriting: "))
speed = int(input("Velosiped tezligini kiriting: "))

if year > 2018 and speed > 24:
  print("Velosiped to'g'ri keladi!")
else:
  print("Velosiped to'g'ri kelmaydi!")

# 2-masala

ball = int(input("Necha ball to'plading? "))
medall = int(input("Medall bormi? "))

if ball > 280 and medall == 1:
  print("Tabriklaymiz! Sen o'qishga kirding!")
else:
  print("Afsuski, sen bizning universitetimizga o'ta olmading.")

# 3-masala

c = int(input("Muhitdagi haroratni kiriting: "))

if c < 0 or c > 100:
  print("Muhitda xavf bor!")