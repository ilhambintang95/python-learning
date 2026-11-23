#Operator Aritmatika
print(3+4)  # Penambahan digunakan untuk menambahkan angka
print(3-4)  # Pengurangan digunakan untuk mengurangkan angka
print(4-3)  # Pengurangan digunakan untuk mengurangkan angka
print(3/4)  # Pembagian digunakan untuk membagi angka
print(4/3)  # Pembagian digunakan untuk membagi angka
print(3*4)  # Perkalian digunakan untuk mengalikan angka
print(3%4)  # Modulus digunakan mencari sisa pembagian dari suatu angka dengan angka lainnya. 3 tidak bisa dibagi 4 maka seluruh angka 3 menjadi sisa nya
print(4%3)  # Modulus digunakan mencari sisa pembagian dari suatu angka dengan angka lainnya. 4 dibagi 3 hanya bisa dibagi 3 selama 1 kali dan menyisakan 1 angka
print(3**4) # Exponential digunakan untuk melakukan pemangkatan dari angka
print(4**3) # Exponential digunakan untuk melakukan pemangkatan dari angka
print(3//4) # FloorDivisionOperator digunakan untuk melakukan pembagian dan langsung membulatkan hasilnya ke bawah ke bilangan bulat terdekat. 3/4 adalah 0.75 jadi dibulatkan kebawah sama dengan 0
print(4//3) # floordivisionoperator digunakan untuk melakukan pembagian dan langsung membulatkan hasilnya ke bawah ke bilangan bulat terdekat. 4/3 adalah 1.333 jadi dibulatkan kebawah sama dengan 1

#Fungsi Matematika

#round(x, n) digunakan untuk membulatkan angka x ke bilangan terdekat atau sejumlah n angka di belakang koma
print(round(3/4, 1)) # 3/4 adalah 0.75. Apabila n 0 maka dibulatkan ke angka bulat terdekat yaitu 1, apabila n 1 maka dibulatkan ke angka belakang koma terdekat yaitu 0.8 dst
print(round(4/3, 1)) # 4/3 adalah 1.3333.... Apabila n 0 maka dibulatkan ke angka bulat terdekat yaitu 1, apabila n 1 maka dibulatkan ke angka belakang koma terdekat yaitu 1.3 dst

#abs(x) digunakan untuk mengubah angka negatif menjadi positif (nilai mutlak)
print(abs(-3))   # mengubah angka -3 menjadi 3
print(abs(-4))   # mengubah angka -4 menjadi 4

#pow(x, y) digunakan untuk menghitung perpangkatan sama seperti **, x pangkat y
print(pow(3, 4))    # 3 pangkat 4 adalah 81
print(pow(4, 3))    # 4 pangkat 3 adalah 64

#divmod(x, y) digunakan sebagai bentuk pengganti (//) untuk x dan (%) untuk y.
print(divmod(3, 4)) # untuk x adalah 3//4 yaitu 0 dan untuk y adalah 3%4 yaitu 3
print(divmod(4, 3)) # untuk x adalah 4//3 yaitu 1 dan untuk y adalah 4%3 yaitu 1

#string harus disertai dengan ("")
print("Ilham")
print("Bintang")
print("Indonesia")
print("Learning reservoir engineering")

name = "Ilham Bintang"
nationality = "Indonesia"
age = 31
price = 123456.789

#f-string untuk menyisipkan nilai variabel atau perhitungan langsung ke dalam teks dengan lebih ringkas dan rapi.
print(f"My name is {name}, I lived in {nationality}, and I am {age} years old.") # digunakan untuk menambahkan format penulisan (,), (.), operasi matematika, fungsi, format angka, dll.
print(f"I was born in {nationality}.")
print(f"4 years later i will be {age+4} years old.")
print(f"Hello, {name.upper()}!") # Tanda kurung () setelah upper berfungsi sebagai tombol "eksekusi" atau "jalankan"
print(f"Total price are: US${price:,}")

#list kumpulan data yang dimasukkan kedalam tanda [] dan dapat dipanggil berdasarkan indeks[] dimulai dari 0. Bisa duplikat dan dapat dirubah dan ditambahkan.
fruit = ["Apple", "Mango", "Orange"]
print(fruit[1])                 # Memanggil data pakai nomor urutan (indeks)
fruit[0] = "Lemon"              # Mengganti sesuai indeks dengan yang diinginkan, indeks[0] Apple diganti jadi Lemon
fruit.append("Watermelon")      # Menambah buah di akhir daftar gunakan append
print(fruit)                    # Print
fruit.insert(0, "Papaya")       # Menambahkan buah di awal daftar gunakan insert.
print(fruit)                    # Print

#tuple kumpulan data yang dimasukkan kedalam tanda () dan dapat dipanggil berdasarkan indeks[] dimulai dari 0. Bisa duplikat, namun tuple tidak dapat dirubah dan ditambahkan.
day = ("Monday", "Tuesday", "Wednesday", "Monday")
print(day)       # Output: ("Monday", "Tuesday", "Wednesday", "Monday") -> Duplikat aman
print(day[1])    # Memanggil data pakai nomor urutan (indeks)
# hari[0] = "Minggu" -> Ini akan ERROR karena tuple tidak bisa diubah

#set kumpulan data yang dimasukkan kedalam tanda {} namun tidak dapat dipanggil berdasarkan indeks[]. Apabila ada duplikat maka data kembar otomatis hilang, namun data dapat dirubah dan ditambahkan.
number = {5, 10, 20, 30, 30, 50, 60}
print(number)       
number.add(40)                  # Menambah data baru dengan add
number.discard(5)               # Menghilangkan data dengan discard
print(number)                   # Print output
number_sort = sorted(number)    # Mengurutkan data  
print(number_sort)              # Print output
# print(angka[0]) -> Ini akan ERROR karena set tidak punya urutan/indeks

#dictionary adalah kumpulan data secara berpasangan dengan format "key" : "value"
profile = {
    "skill": "PVT",
    "city": "Jakarta",
    "experiences": "8 years"
}
# Memanggil data pakai kata kunci (key), bukan angka
print(profile["skill"])     # Print output skill : PVT
# Mengubah dan menambah data
profile["experiences"] = "9 years"       # Mengubah nilai umur
print(profile["experiences"])      # Print output umur
profile["hobi"] = "Coding"  # Menambah pasangan key-value baru

#check type data
print(type(age))
print(type(price))
print(type(name))
print(type(day))
print(type(fruit))
print(type(number))
print(type(profile))

#euclidean distance
#d(p,q)**=(q1-p1)**2+(q2-p2)**2
p1 = 2
q1 = 10
p2 = 3
q2 = 8

import math
euclidean_distance = math.sqrt(((q1-p1)**2)+((q2-p2)**2))
print(euclidean_distance)

print(profile)

#radius circle is 30 meters
import math

rad = 30
area_of_circle = math.pi*(rad**2)
circum_of_circle = math.pi*2*rad

print(f"Area of Circle = {area_of_circle:.2f}m\u00b2")
print(f"Circumferences of Circle = {circum_of_circle:.2f} metres")

print("-"*40)

defined_rad = float(input("Radius of the circle (metre): "))
user_area = math.pi*(defined_rad**2)
print(f"Area of circle with Radius {defined_rad} m = {user_area:.2f}m\u00b2")