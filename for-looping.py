max = int(input("masukan nilai :"))

#bintang berkurang
for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()

#dari kanan ke kiri (kurang)
for i in range(max):
    # Tambahkan spasi untuk menggeser pola ke kanan
    print("  " * i, end="")
    for j in range(max - i):
        print("*", end=" ")
    print()

#dari kanan ke kiri (tambah)
for i in range(1, max + 1):
    print("  " * (max - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()   

#bintang  bertambah
for i in range(1, max + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#bintang segitiga
for i in range(1, max + 1):
    # Cetak spasi
    for j in range(max - i):
        print(" ", end="")
    # Cetak bintang
    for k in range(2 * i - 1):
        print("*", end="")
    # Pindah ke baris berikutnya
    print()