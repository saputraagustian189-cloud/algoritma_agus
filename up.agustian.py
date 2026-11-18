nama = input("masukkan nama barang: ")
stok = int(input("masukkan stok awal: "))

while True:
    print("\n1. barang Masuk")
    print("2. barang Keluar")
    print("3. selesai")

    pilih = input("pilih: ")

    if pilih == "1":
        jumlah = int(input("jumlah masuk: "))
        stok = stok + jumlah

    elif pilih == "2":
        jumlah = int(input("jumlah keluar: "))

        if jumlah > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok = stok - jumlah

    elif pilih == "3":
        print("Nama barang:", nama)
        print("Stok akhir:", stok)
        break

    else:
        print("Pilihan salah!")