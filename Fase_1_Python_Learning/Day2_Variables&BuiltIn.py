# Excercises 1
first_name = "Ilham"
last_name = "Bintang"
full_name = "Ilham Bintang"
nationality = "Indonesia"
city = "Jakarta"
age = 31
year_of_birth = 1995
is_married = True
is_true = True
is_light_on = True

#len digunakan untuk menghitung panjang(length) karakter dari sebuah value
print(len(first_name))  # Panjang karakter dari Ilham adalah 5
print(len(last_name))   # Panjang karakter dari Bintang adalah 7
print(len(full_name))   # Panjang karakter dari Ilham Bintang adalah 13

first_name_len = len(first_name)    # Memberikan variabel atas panjang karakter dari nama depan
last_name_len = len(last_name)      # Memberikan variabel atas panjang karakter dari nama belakang

print("First name longer than last name?", first_name_len > last_name_len)  # Mencetak output True atau False dari logika perbandingan panjang karakter antara nama depan dan nama belakang
print("Last name longer than last name?", first_name_len < last_name_len)   # Mencetak output True atau False dari logika perbandingan panjang karakter antara nama depan dan nama belakang

if first_name_len > last_name_len:          
    print("First name longer than last name")   # Mencetak output True atau False dari logika perbandingan panjang karakter antara nama depan dan nama belakang
if last_name_len > first_name_len:
    print("Last name longer than first name")   # Mencetak output True atau False dari logika perbandingan panjang karakter antara nama depan dan nama belakang

print("-"*40)

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(remainder)
print(exp)
print(floor_division)

print("-"*40)

# Switch data
num_integer = 10
num_float = 10.26
num_str = "10"

#integer to float
print(float(num_integer))   # mengubah data yang awalnya integer menjadi float

#float to integer
print(int(num_float))       # mengubah data yang awalnya float menjadi integer

# integer to string
print(str(num_integer))     # mengubah data yang awalnya integer menjadi string

# string to integer
print(int(num_str))         # mengubah data yang awalnya string menjadi integer

# string to list
print(list(last_name))

# string to tuple
print(tuple(last_name))
print(last_name[1])

print("-"*40)

#radius circle is 30 meters
import math

rad = 30 
area_of_circle = math.pi*(rad**2)   # Rumus luas lingkaran
circum_of_circle = math.pi*2*rad    # Rumus keliling lingkaran

print(f"Area of Circle = {area_of_circle:.3f}m\u00b2")              # print output dengan tulisan Area of Circle dengan f-string, ".xf" dimaksudkan untuk x angka dibelakang koma. \u00b adalah format khusus.
print(f"Circumferences of Circle = {circum_of_circle:.3f} metres")  # print output dengan tulisan Area of Circle dengan f-string, ".xf" dimaksudkan untuk x angka dibelakang koma. \u00b adalah format khusus.

print("-"*40)

defined_rad = float(input("Radius of the circle (metre): "))    # float digunakan untuk mengubah hasil input yang tadinya string menjadi float agar dapat dimasukkan ke rumus defined area
defined_area = math.pi*(defined_rad**2) # rumus luas lingkaran dengan defined rad yang di input
print(f"Area of circle with Radius {defined_rad:.0f} m = {defined_area:.3f}m\u00b2")    # Print output 

