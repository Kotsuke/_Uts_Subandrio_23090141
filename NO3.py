def hitung_total_harga(belanjaan):
    total_harga = sum(harga * jumlah for _, harga, jumlah in belanjaan)
    return total_harga

def main():
    belanjaan = []
    while True:
        nama_barang = input("Masukkan nama barang (ketik 'selesai' untuk selesai): ")
        if nama_barang.lower() == 'selesai':
            break
        harga_barang = float(input("Masukkan harga barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        belanjaan.append((nama_barang, harga_barang, jumlah_barang))

    total = hitung_total_harga(belanjaan)
    print("Total harga belanjaan adalah:", total)

if __name__ == "__main__":
    main()
