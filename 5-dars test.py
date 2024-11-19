# 1-vazifa

a = int(input("Tashqarida yomg'ir yog'yaptimi?: "))

if a == 1:
    print("Yomg'ir yog'moqda. Soyabonni oling!")

if a == 0:
    print("Tashqarida yomg'ir yog'gani yo'q")

# 2-vazifa

a = int(input("Rus tili bo'yicha ballar miqdorini kiriting: "))
b = int(input("Matematika bo'yicha ballar miqdorini kiriting:"))
c = int(input("Informatika bo'yicha ballar miqdorini kiriting:"))

if (a + b +c) >= 270:
    print("Tabriklaymiz! Siz o'qishga byudjet asosida qabul qilindingiz.")
else:
  print("Afsuski, Siz o'qishga byudjet asosida qabul qilinmadingiz.")

# 3-vazifa

a = int(input("Juft sonni kiriting: "))

if a % 2 == 0:
    print("Juft son")
else:
    print("Toq son")

# 4-vazifa

a = int(input("Birinchi mahsulot narhini kiriting: "))
b = int(input("Ikkinchi mahsulot narhini kiriting: "))
c = int(input("Uchinchi mahsulot narhini kiriting: "))

if (a + b + c) > 10000:
  print("Siz shuncha pul to'lashingiz kerak bo'ladi: ", (a + b + c) - (a + b + c) * 10 / 100)
else:
  print("Siz shuncha pul to'lashingiz kerak bo'ladi: ", (a + b + c))

# 5-vazifa

a = int(input("Sonni kiriting: "))

if a > 0:
  print("Javob: ", a)
else:
  print("Javob: ", -a)

# 6-vazifa

a = int(input("Umidning kubiklari soni: "))
b = int(input("Muassasa egasi kubiklari soni: "))

print("Natija: ", a + b)

if a >= b:
  print("Umid to'laydi!")
else:
  print("Muassasa egasi to'laydi!")

print("O'yin tugadi!")

# 7-vazifa

money = int(input("Qancha pul yechib olmoqchisiz? "))

if money % 100 == 0:
  print("Pulni muvaffaqqiyatli yechish mumkin")
else:
  print("Pulni muvaffaqqiyatli yechish mumkin emas")

print("Kuningiz hayrli bo'lsin!")

# 8-vazifa

hours = int(input("Ishlagan soatlar sonini kiriting:  "))
kredit = int(input("Kredit bo'yicha qoldiqni kiriting: "))
lunch = int(input("Ovqatlanish xarajatlarini kiriting: "))

b = (200 * hours) / (2 ** 3) + hours

if b >= (kredit + lunch):
   print("Soatlar yetarli, dam olish mumkin!")
else:
  print("Soatlar yetarli emas, Ishlash kerak!")

# 9-vazifa

s = int(input("Bosib o'tilgan yo'lni kiriting: "))
day = int(input("Kunlar sonini kiriting: "))

if (s // 100) + (s // 10 % 10) + (s % 10) > day:
  s = 0
  print("Sonlarni tashlab yuborish!")
  print(s)
else:
  print("Bugun buzilmadi!")

print("Bosib o'tilgan yo'l: ", s, "ga teng")

# 10-vazifa

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

if a > (b + c) / 2:
  print("Birinchi son katta", "ya'ni", a)

if b > (a + c) / 2:
  print("Ikkinchi son katta", "ya'ni", b)

if c > (a + b) / 2:
  print("Uchinchi son katta", "ya'ni", c)