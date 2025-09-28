# Main
print("+============================================+")
print("|    Nama      : Ghea Aisyah Windraswari     |")
print("|    Prodi     : Sistem Informasi A          |")
print("|    Praktikum : Dasar Dasar Pemrograman     |")
print("|    Program  : Mini Project 2               |")
print("+============================================+")

# Program Sistem Pencatat Password Aplikasi
from prettytable import PrettyTable
from pwinput import pwinput

Menu_Admin = ("Tambah Password", "Lihat Password", "Ubah Password", "Hapus Password", "Keluar")
Menu_Pengguna = ("Tambah Password", "Lihat Password", "Ubah Password", "Keluar")

Data_Tersimpan = [
    {"Aplikasi": "Instagram", "Username": "gheaisywr", "Password": "Abc12345"}, 
    {"Aplikasi": "Spotify", "Username": "kambingguling", "Password": "gatau098"}, 
    {"Aplikasi": "YouTube", "Username": "dasterpink", "Password": "manasayatau135"},
    {"Aplikasi": "FaceBook", "Username": "jualbelimusang", "Password": "aigoo23124"},
    {"Aplikasi": "Twitter", "Username": "kia.nsantang", "Password": "yahahahayu00"},
    {"Aplikasi": "Threads", "Username": "bbiarapaa", "Password": "biarinaja21"},
    {"Aplikasi": "TikTok", "Username": "zakit_kepala50", "Password": "butuhpertolongan"},
    {"Aplikasi": "TikTok", "Username": "nemokrasii", "Password": "17plusdelapan"}
]

# Role 
Pengguna = {
    "admin": {"Password": "12345", "Role": "admin"},
    "user": {"Password": "abcde", "Role": "user"}
}

# LOGIN
def login():
    while True:
        print("\n💻 Hallo! Selamat Datang di Sistem Pencatat Password!\n")
        username = input("Masukkan Username: ")
        password = pwinput("Masukkan Password: ")
        if username in Pengguna and Pengguna[username]["Password"] == password:
            print(f"\n Login berhasil! Selamat Datang, {username}!\n")
            return Pengguna[username]["Role"]
        else:
            print("Login Gagal! Username atau Password Salah. Coba lagi.\n")

# Fungsi CRUD
def tambah_password():
    print("\n(Tambah Password)")
    Aplikasi = input("Masukkan Aplikasi: ")
    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")

    data_baru = {"Aplikasi": Aplikasi, "Username": Username, "Password": Password}
    Data_Tersimpan.append(data_baru)
    print("-------------------------------------------------")
    print("Yey! Data Password Kamu Berhasil ditambahkan!")
    print("-------------------------------------------------")
    table = PrettyTable()
    table.field_names = ["Aplikasi", "Username", "Password"]
    table.add_row([Aplikasi, Username, Password])
    print(table)

def lihat_password():
    print("\n(Lihat Password)")
    print("=================================================")
    if not Data_Tersimpan:
        print("Belum Ada Data Tersimpan")
        return
    
    table = PrettyTable()
    table.field_names = ["No", "Aplikasi", "Username", "Password"]
    for i, data in enumerate(Data_Tersimpan):
        table.add_row([i, data["Aplikasi"], data["Username"], data["Password"]])
    print(table)

def ubah_password():
    lihat_password()
    if not Data_Tersimpan:
        return
    try:
        idx = int(input(f"Pilih Nomor Data Untuk Mengubah Password (1-{len(Data_Tersimpan)-1}): "))
        if 0 <= idx < len(Data_Tersimpan):
            Password_Baru = input("Masukkan Password Baru: ")
            Data_Tersimpan[idx]["Password"] = Password_Baru
            print("\n Data berhasil diperbarui!\n")
            lihat_password()
        else:
            print("Nomor Tidak Valid!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_password():
    lihat_password()
    if not Data_Tersimpan:
        return
    
    try:
        nomor = int(input("Pilih Nomor Data Yang Ingin Dihapus: "))
        if 0 <= nomor < len(Data_Tersimpan):
            hapus = Data_Tersimpan.pop(nomor)
            print(f"\n Data {hapus['Aplikasi']} berhasil dihapus!\n")
            lihat_password()
        else:
            print("Nomor Tidak Valid")
    except ValueError:
        print("Input harus berupa angka!")

def keluar():
    print("Terima kasih telah menggunakan program ini!")
    exit()

# Main Program
while True:
    role = login()
    if role == "admin":
        while True:
            print("\n===== MENU ADMIN =====")
            print("1. Tambah Password")
            print("2. Lihat Password")
            print("3. Ubah Password")
            print("4. Hapus Password")
            print("5. Keluar")
            
            try:
                Pilihan = int(input("Silahkan Pilih Menu (1-5): "))
                if Pilihan == 1:
                    tambah_password()
                elif Pilihan == 2:
                    lihat_password()
                elif Pilihan == 3:
                    ubah_password()
                elif Pilihan == 4:
                    hapus_password()
                elif Pilihan == 5:
                    keluar()
                else:
                    print("Pilihan Tidak Valid!")
            except ValueError:
                print("Input harus berupa angka!")

    elif role == "user":
        while True:
            print("\n===== MENU USER =====")
            print("1. Tambah Password")
            print("2. Lihat Password")
            print("3. Ubah Password")
            print("4. Keluar")

            try:
                Pilihan = int(input("Pilih Menu (1-4): "))
                if Pilihan == 1:
                    tambah_password()
                elif Pilihan == 2:
                    lihat_password()
                elif Pilihan == 3:
                    ubah_password()
                elif Pilihan == 4:
                    print("Keluar dari Program")
                    break
                else:
                    print("Pilihan Tidak Valid!")
            except ValueError:
                print("Input harus berupa angka!")
