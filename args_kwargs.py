
def tampilkan(*args):
    "fungsi tampilkan buah"
    for n, buah in enumerate(args, start=1):
        print("{0}. {1}".format(n, buah))

print("Toko Buah Koperasi UNJANI Yogyakarta")
jumlah = int(input("Masukan banyaknya buah yang dibeli: "))
list_buah = []
for i in range(1, jumlah+1):
    buah = input(f"Buah {i}: ")
    list_buah.append(buah)

print("Buah yang anda beli adalah")
tampilkan(*list_buah)
print("Terima Kasih...")
"""
"""
def mahasiswa(nama, nim, prodi, hobi):
    "fungsi tampilkan data mahasiswa"
    print("Mahasiswa Prodi {0} UNJANI Yogyakarta".format(prodi))
    print("Dengan nama {0}".format(nama))
    print("Mempunyai NIM {0}".format(nim))
    print("Memiliki hobi {0}".format(hobi))

print("Profile Mahasiswa UNJANI Yogyakarta")
nama = input("Nama: ")
nim = input("NIM: ")
prodi = input("Prodi: ")
hobi = input("Hobi: ")
data = {'nama': nama, 'nim': nim, 'prodi': prodi, 'hobi': hobi}
mahasiswa(**data)



    