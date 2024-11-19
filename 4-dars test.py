# 1-vazifa

a = 8
b = 10
c = 12
d = 18

print(((-3 + a ** 2) * (b - 2 ** 3)) / (c - 2 * d))

# 2-vaifa

a = int(input("Birinchi raqamni kiriting: "))
b = int(input("Ikkinchi raqamni kiriting: "))
c = int(input("Uchinchi raqamni kiriting: "))
d = int(input("To'rtinchi raqamni kiriting: "))

print((a + b) / (c + d))

# 3-vaifa

a = int(input("Raqamni kiriting: "))

print(a, "raqamidan so'ng", a + 1, "raqami keladi")
print(a, "raqamidan oldin", a - 1, "raqami turadi")

# 4-vazifa

a = int(input("1 - katet uzunligini kiriting: "))
b = int(input("2 - katet uzunligini kiriting: "))

print("Uchburchakning yuzi: ", (a * b) / 2, "ga teng")

# 5-vazifa

a = int(input("Daqiqalar sonini kiriting: "))

print(a // 60, "soat", a % 60, "minut",)

# 6-vazifa

a = int(input("Birinchi raqamni yozing: "))
b = int(input("Ikkinchi raqamni yozing: "))

print("Natija: ", (a % 10) + (b % 10))

# 7-vazifa

v = int(input("Tezlikni kiriting: "))
t = int(input("Vaqtni kiriting: "))

print("Ibrohim", (v * t) // 115, "ta aylanani to'liq yugurgan")
print("Ibrohim keyingi aylanani", (v * t) % 115, "km yugurgan")

# 8-vazifa

a = int(input("To'rt xonali sonni kiriting: "))

print(a // 1000)
print(a // 100 % 10)
print(a // 10 % 10)
print(a % 10)

# 9-vazifa

a = int(input("To'rt xonali sonni kiriting: "))

print(a % 10, a // 10 % 10, a // 100 % 10, a // 1000)

# 10-vazifa

a = int(input("Birinchi raqamni kiriting: "))
b = int(input("Ikkinchi raqamni kiriting: "))

print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)