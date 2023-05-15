#Latihan 1
#Amanda Rismawati
#10109005

stack = []

def buku_tambahan(stack, NamaBuku, Pengarang):
    BukuBaru = [NamaBuku, Pengarang]
    stack.append(BukuBaru)
    print(f"{BukuBaru} berhasil ditambahkan ke dalam stack.")

def hapus_buku_terakhir(stack):
    if len(stack)==0:
        print("Stack kosong, tidak terdapat buku yang bisa dihapus.")
    else:
        buku_terakhir = stack.pop()
        print(f"{buku_terakhir} berhasil dihapus dari stack.")

def tampilkan_buku_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak terdapat buku yang tidak bisa ditampilkan.")
    else:
        buku_teratas = stack[-1]
        print(f"Buku teratas yang berada di dalam stack adalah {buku_teratas}.")

while True :
    print("\nTumpukan buku saat ini: ", stack)
    print("Menu :")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Buku yang keluar")

    pilihan = input("Masukan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        NamaBuku = input("Masukan nama buku yang ingin kamu tambahkan: ")
        Pengarang = input("Masukan nama pengarang yang ingin kamu tambahkan: ")
        buku_tambahan(stack, NamaBuku, Pengarang)
    elif pilihan == "2":
        hapus_buku_terakhir (stack)
    elif pilihan == "3":
        tampilkan_buku_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        
