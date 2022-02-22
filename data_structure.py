#   Nama    : Ilham Mulia
#   Prodi   : Informatika
#   NIM     : 212102007


biodata = {
    'nama' : ['Setrika Panasonic', 'Kipas Toshiba', 'Raket Nyamuk'],
    'stok' : ['4', '3', '2'],
    'harga' : ['100000', '150000', '560000']
}
for i in range(len(biodata)):
    print(i, ". ", biodata['nama'][i])
print()
pilih = int(input("Masukan nomor barang: "))
print("""
---------------------------------------------
Nama Produk             Stok        Harga
=============================================
""")
print(biodata['nama'][pilih]," ", biodata['stok'][pilih]," ", biodata['harga'][pilih])