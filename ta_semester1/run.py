import json, sys, os
import random
from datetime import datetime
try:
    import pytz
except:
    os.system("pip install pytz")
    import pytz

db_path = 'database'
wib = pytz.timezone('Asia/Jakarta')
date = datetime.now(wib).strftime('%d-%m-%Y %H:%M:%S')

if not os.path.exists(db_path):
    os.makedirs(db_path)

session = None

def cari_id(id):
    file = open(f'{db_path}/pegawai.json', 'r+')
    read = json.load(file)
    for pegawai in read['pegawai']:
        for key, value in pegawai.items():
            if value == id:
                output = True
            else:
                output = False
    return output
        
    
def log_aktivitas(data = None):
    if data is not None:
        file = open(f'{db_path}/log_aktivitas.txt', 'a+')
        file.write(data + "\n")
        file.close()
    else:
        file = open(f'{db_path}/log_aktivitas.txt', 'r').read()
        print(file)

def login_pegawai(id, password):
    global session
    try:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        for pegawai in read['pegawai']:
            if pegawai['id_pegawai'] == id:
                if pegawai['password'] == str(password):
                    session = f"{id} - {pegawai['nama']}"
                    log_aktivitas(f'[{date}][{session}] Telah login.')
                    return True
                    break
                else:
                    return "[~] Kata sandi salah."
            else:
                pass
    except Exception as e:
        return f"[~] Login error. Error: {e}"

def logout_pegawai():
    global session
    try:
        log_aktivitas(f'[{date}][{session}] Telah logout.')
        session = None
        return True
    except Exception as e:
        return f"[~] Logout error. Error: {e}"

def data_pegawai(id = None):
    if id is not None:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        new_data = []
        for pegawai in read['pegawai']:
            if pegawai['id_pegawai'] == id:
                pegawai.clear()
            else:
                data = {"id_pegawai": pegawai['id_pegawai'], 'nama': pegawai['nama'], 'jabatan': pegawai['jabatan']}
                new_data.append(data)
        fp = open(f'{db_path}/data_pegawai.json', 'w')
        json.dump(new_data, fp, indent=4)
    else:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        list = []
        with open(f'{db_path}/data_pegawai.json', 'r+') as fp:
            for pegawai in read['pegawai']:
                data = {"id_pegawai": pegawai['id_pegawai'], 'nama': pegawai['nama'], 'jabatan': pegawai['jabatan']}
                list.append(data)
            json.dump(list, fp, indent=4)
        
    
def tambah_pegawai(id, password, nama, jabatan, jk):
    try:
        data = {
            "id_pegawai": id,
            "password": str(password),
            "nama": str(nama),
            "jabatan": str(jabatan),
            "jk": str(jk)
        }
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        read['pegawai'].append(data)
        with open(f'{db_path}/pegawai.json', 'w') as fp:
            json.dump(read, fp, indent=4)
        data_pegawai()
        log_aktivitas(f'[{date}][{session}] Telah menambahkan data pegawai dengan id {id}.')
        return True
    except Exception as e:
        return f"[~] Tambah pegawai gagal. Error: {e}"

def hapus_pegawai(id):
    try:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        new_data = {"pegawai": []}
        for pegawai in read['pegawai']:
            if pegawai['id_pegawai'] == id:
                pegawai.clear()
            else:
                new_data['pegawai'].append(pegawai)
        fp = open(f'{db_path}/pegawai.json', 'w')
        json.dump(new_data, fp, indent=4)
        log_aktivitas(f'[{date}][{session}] Telah menghapus data pegawai dengan id {id}.')
        return True
    except Exception as e:
        return f"[~] Hapus data pegawai gagal. Error: {e}"
    
def info_pegawai(id):
    try:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        for pegawai in read['pegawai']:
            if pegawai['id_pegawai'] == id:
                print(f"""
--------------------------------
        Informasi Pegawai
--------------------------------
ID Pegawai    : {pegawai['id_pegawai']}
Nama Pegawai  : {pegawai['nama']}
Jabatan       : {pegawai['jabatan']}
Jenis Kelamin : {pegawai['jk']}
                  """)
            else:
                pass
        return True
    except Exception as e:
        return f"[~] ID Pegawai tidak ditemukan. Error: {e}"

def ubah_pegawai(id):
    try:
        file = open(f'{db_path}/pegawai.json', 'r+')
        read = json.load(file)
        for pegawai in read['pegawai']:
            if pegawai['id_pegawai'] == id:
                nama = input("Masukan Nama Pegawai: ")
                jabatan = input("Masukan Jabatan Pegawai: ")
                jk = input("Masukan Jenis Kelamin Pegawai: ")
                password = input("Masukan Kata Sandi Pegawai: ")
                hapus = hapus_pegawai(id)
                if hapus != True:
                    print(hapus)
                    ubah_pegawai(id)
                else:
                    tambah = tambah_pegawai(id, password, nama, jabatan, jk)
                    if tambah != True:
                        print(tambah)
                        ubah_pegawai(id)
                    else:
                        log_aktivitas(f'[{date}][{session}] Telah mengubah data pegawai dengan id {id}.')
                        return True
    except Exception as e:
        return f"[~] Ubah data pegawai gagal. Error: {e}"
    
def menu_login():
    print("""       
--------------------------------
         Halaman Admin
--------------------------------
1. Login Pegawai
2. Keluar Program 
""")
    try:
        pilihan = int(input("Masukan pilihan anda: "))
        if pilihan == 1:
            id_pegawai = int(input("\nMasukan ID Pegawai: "))
            password = input("Masukan Kata Sandi: ")
            check_login = login_pegawai(id_pegawai, password)
            if check_login != True:
                print(check_login)
                menu_login()
            else:
                menu_home()
        elif pilihan == 2:
            sys.exit()
        else:
            print("[~] Pilihan tidak tersedia.")
            menu_login()
    except ValueError:
        print("[~] Masukan angka. Coba lagi.")
        menu_login()
    except Exception as e:
        return f"[~] Program error. Error: {e}"
    
def menu_pegawai():
    global session
    if session == None:
        menu_login()
    else:
        print("""       
--------------------------------
        Menu Pegawai
--------------------------------
1. Tambah Pegawai
2. Hapus Pegawai
3. Update Pegawai
4. Informasi Pegawai
5. Kembali
""")
        try:
            pilihan = int(input("Masukan pilihan anda: "))
            if pilihan == 1:
                id_pegawai = random.randint(100000, 999999)
                nama = input("Masukan Nama Pegawai: ")
                jabatan = input("Masukan Jabatan Pegawai: ")
                jk = input("Masukan Jenis Kelamin Pegawai: ")
                password = input("Masukan Kata Sandi Pegawai: ")
                while cari_id(id_pegawai) == True:
                    id_pegawai = random.randint(100000, 999999)
                tambah = tambah_pegawai(id_pegawai, password, nama, jabatan, jk)
                if tambah != True:
                    print(tambah)
                    menu_pegawai()
                else:
                    print('[~] Tambah data pegawai berhasil.')
                    menu_pegawai()
            elif pilihan == 2:
                id_pegawai = int(input("Masukan ID Pegawai: "))
                hapus = hapus_pegawai(id_pegawai)
                if hapus != True:
                    print(hapus)
                    menu_pegawai()
                else:
                    print('[~] Hapus data pegawai berhasil.')
                    data_pegawai(id_pegawai)
                    menu_pegawai()
            elif pilihan == 3:
                id_pegawai = int(input("Masukan ID Pegawai: "))
                ubah = ubah_pegawai(id_pegawai)
                if ubah != True:
                    print(ubah)
                    menu_pegawai()
                else:
                    print('[~] Ubah data pegawai berhasil.')
                    menu_pegawai()
            elif pilihan == 4:
                id_pegawai = int(input("Masukan ID Pegawai: "))
                info_pegawai(id_pegawai)
                menu_pegawai()
            elif pilihan == 5:
                menu_home()
        except:
            return "[~] Program error."
        
def cari_barang(id):
    file = open(f'{db_path}/barang.json', 'r+')
    read = json.load(file)
    for barang in read['barang']:
        for key, value in barang.items():
            if value == id:
                output = True
            else:
                output = False
    return output
        
def data_barang(id = None):
    if id is not None:
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        new_data = []
        for barang in read['barang']:
            if barang['id_barang'] == id:
                barang.clear()
            else:
                data = {"nama": barang['nama'], "jenis": barang['jenis'], "stok": barang['stok']}
                new_data.append(data)
        fp = open(f'{db_path}/data_barang.json', 'w')
        json.dump(new_data, fp, indent=4)
    else:
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        list = []
        with open(f'{db_path}/data_barang.json', 'r+') as fp:
            for barang in read['barang']:
                data = {"nama": barang['nama'], "jenis": barang['jenis'], "stok": barang['stok']}
                list.append(data)
            json.dump(list, fp, indent=4)
            
def tambah_barang(id, nama, jenis, stok):
    try:
        data = {
            "id_barang": id,
            "nama": str(nama),
            "jenis": str(jenis),
            "stok": stok
        }
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        read['barang'].append(data)
        with open(f'{db_path}/barang.json', 'w') as fp:
            json.dump(read, fp, indent=4)
        data_barang()
        log_aktivitas(f'[{date}][{session}] Telah menambahkan data barang dengan id {id}.')
        return True
    except Exception as e:
        return f"[~] Tambah barang gagal. Error: {e}"

def hapus_barang(id):
    try:
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        new_data = {"barang": []}
        for pegawai in read['barang']:
            if pegawai['id_barang'] == id:
                pegawai.clear()
            else:
                new_data['barang'].append(pegawai)
        fp = open(f'{db_path}/barang.json', 'w')
        json.dump(new_data, fp, indent=4)
        log_aktivitas(f'[{date}][{session}] Telah menghapus data barang dengan id {id}.')
        return True
    except Exception as e:
        return f"[~] Hapus data barang gagal. Error: {e}"
    
def info_barang(id):
    try:
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        for barang in read['barang']:
            if barang['id_barang'] == id:
                print(f"""
--------------------------------
        Informasi Barang
--------------------------------
ID Barang       : {barang['id_barang']}
Nama Barang     : {barang['nama']}
Jenis Barang    : {barang['jenis']}
Stok            : {barang['stok']}
                  """)
            else:
                pass
        return True
    except Exception as e:
        return f"[~] ID Barang tidak ditemukan. Error: {e}"
    
def ubah_barang(id):
    try:
        file = open(f'{db_path}/barang.json', 'r+')
        read = json.load(file)
        for barang in read['barang']:
            if barang['id_barang'] == id:
                nama = input("Masukan Nama Barang: ")
                jenis = input("Masukan Jenis Barang: ")
                stok = input("Masukan Stok Barang: ")
                hapus = hapus_barang(id)
                if hapus != True:
                    print(hapus)
                    ubah_barang(id)
                else:
                    tambah = tambah_barang(id, nama, jenis, stok)
                    if tambah != True:
                        print(tambah)
                        ubah_barang(id)
                    else:
                        log_aktivitas(f'[{date}][{session}] Telah mengubah data barang dengan id {id}.')
                        return True
    except Exception as e:
        return f"[~] Ubah data barang gagal. Error: {e}"
    
def menu_barang():
    global session
    if session == None:
        menu_login()
    else:
        print("""       
--------------------------------
          Menu Barang
--------------------------------
1. Tambah Barang
2. Hapus Barang
3. Update Barang
4. Informasi Barang
5. Kembali
""")
        try:
            pilihan = int(input("Masukan pilihan anda: "))
            if pilihan == 1:
                id_barang = random.randint(100000, 999999)
                nama = input("Masukan Nama Barang: ")
                jenis = input("Masukan Jenis Barang: ")
                stok = int(input("Masukan Stok Barang: "))
                while cari_barang(id_barang) == True:
                    id_barang = random.randint(100000, 999999)
                tambah = tambah_barang(id_barang, nama, jenis, stok)
                if tambah != True:
                    print(tambah)
                    menu_barang()
                else:
                    print('[~] Tambah data barang berhasil.')
                    menu_barang()
            elif pilihan == 2:
                id_barang = int(input("Masukan ID Barang: "))
                hapus = hapus_barang(id_barang)
                if hapus != True:
                    print(hapus)
                    menu_barang()
                else:
                    print('[~] Hapus data barang berhasil.')
                    data_barang(id_barang)
                    menu_barang()
            elif pilihan == 3:
                id_barang = int(input("Masukan ID Barang: "))
                ubah = ubah_barang(id_barang)
                if ubah != True:
                    print(ubah)
                    menu_barang()
                else:
                    print('[~] Ubah data barang berhasil.')
                    menu_barang()
            elif pilihan == 4:
                id_barang = int(input("Masukan ID Barang: "))
                info_barang(id_barang)
                menu_barang()
            elif pilihan == 5:
                menu_home()
        except:
            return "[~] Program error."
        
def menu_home():
    global session
    if session == None:
        menu_login()
    else:
        print("""       
--------------------------------
           Menu Home
--------------------------------
1. Menu Pegawai
2. Menu Barang
3. Log Aktivitas
4. Logout
""")
    try:
        pilihan = int(input("Masukan pilihan anda: "))
        if pilihan == 1:
            menu_pegawai()
        elif pilihan == 2:
            menu_barang()
        elif pilihan == 3:
            log_aktivitas()
            menu_home()
        elif pilihan == 4:
            logout = logout_pegawai()
            if logout != True:
                print(logout)
                menu_home()
            else:
                menu_login()
    except:
        return "[~] Program error."
    
    
print("""
--------------------------------
   Program Inventaris Gudang
--------------------------------

""")
try:
    menu_login()
except:
    print("[~] Program error.")

        
        
        
        