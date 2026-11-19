#Operator Aritmatika
print(3+4)  #Penambahan digunakan untuk menambahkan angka
print(3-4)  #Pengurangan digunakan untuk mengurangkan angka
print(4-3)  #Pengurangan digunakan untuk mengurangkan angka
print(3/4)  #Pembagian digunakan untuk membagi angka
print(4/3)  #Pembagian digunakan untuk membagi angka
print(3*4)  #Perkalian digunakan untuk mengalikan angka
print(3%4)  #Modulus digunakan mencari sisa pembagian dari suatu angka dengan angka lainnya. 3 tidak bisa dibagi 4 maka seluruh angka 3 menjadi sisa nya
print(4%3)  #Modulus digunakan mencari sisa pembagian dari suatu angka dengan angka lainnya. 4 dibagi 3 hanya bisa dibagi 3 selama 1 kali dan menyisakan 1 angka
print(3**4) #Exponential digunakan untuk melakukan pemangkatan dari angka
print(4**3) #Exponential digunakan untuk melakukan pemangkatan dari angka
print(3//4) #FloorDivisionOperator digunakan untuk melakukan pembagian dan langsung membulatkan hasilnya ke bawah ke bilangan bulat terdekat. 3/4 adalah 0.75 jadi dibulatkan kebawah sama dengan 0
print(4//3) #floordivisionoperator digunakan untuk melakukan pembagian dan langsung membulatkan hasilnya ke bawah ke bilangan bulat terdekat. 4/3 adalah 1.333 jadi dibulatkan kebawah sama dengan 1

#Fungsi Matematika

#round(x, n) digunakan untuk membulatkan angka x ke bilangan terdekat atau sejumlah n angka di belakang koma
print(round(3/4, 1)) #3/4 adalah 0.75. Apabila n 0 maka dibulatkan ke angka bulat terdekat yaitu 1, apabila n 1 maka dibulatkan ke angka belakang koma terdekat yaitu 0.8 dst
print(round(4/3, 1)) #4/3 adalah 1.3333.... Apabila n 0 maka dibulatkan ke angka bulat terdekat yaitu 1, apabila n 1 maka dibulatkan ke angka belakang koma terdekat yaitu 1.3 dst

#abs(x) digunakan untuk mengubah angka negatif menjadi positif (nilai mutlak)
print(abs(-3))   #mengubah angka -3 menjadi 3
print(abs(-4))   #mengubah angka -4 menjadi 4

#pow(x, y) digunakan untuk menghitung perpangkatan sama seperti **, x pangkat y
print(pow(3, 4))    #3 pangkat 4 adalah 81
print(pow(4, 3))    #4 pangkat 3 adalah 64

#divmod(x, y) digunakan sebagai bentuk pengganti (//) untuk x dan (%) untuk y.
print(divmod(3, 4)) #untuk x adalah 3//4 yaitu 0 dan untuk y adalah 3%4 yaitu 3
print(divmod(4, 3)) #untuk x adalah 4//3 yaitu 1 dan untuk y adalah 4%3 yaitu 1