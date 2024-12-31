perpus = {} # daftar buku yang disimpan dalam bentuk dictionary

def tambah_buku(): # prosedur untuk menambahkan buku
    print("\n")

    # Lakukan perulangan sampai ID yang dimasukkan pengguna sudah benar
    while True:
        id_buku = input("Masukkan ID Buku: ") # Meminta pengguna untuk memasukkan ID Buku

        # Cek apakah buku dengan id tersebut sudah ada
        if id_buku in perpus: 
            # jika sudaha ada
            print("Buku dengan ID tersebut sudah ada, Mohon Masukkan ID yang lain!")
        else:
            break # Jika ID buku belum ada maka keluar dari loop dan lanjutkan
                  # proses penginputan informasi buku

    # Minta pengguna untuk memasukkan informasi buku
    judul_buku = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Penulis: ")
    kategori = input("Masukkan Kategori: ")

    # Menyimpan informasi buku ke dalam dictionary dengan ID Buku sebagai Key
    perpus[id_buku] = {
        'judul_buku': judul_buku,
        'penulis': penulis,
        'kategori': kategori
    }

    print("\nBuku Berhasil Ditambahkan!\n")

def cari_buku(): # prosedur untuk mencari buku berdasarkan id atau judul buku
    if not perpus: # Memeriksa apakah daftar buku kosong
        print("\nDaftar Buku Masih Kosong\n")
        return # kembali ke menu utama karena isi daftar buku masih kosong
    
    # Meminta pengguna untuk memasukkan ID Buku / Judul Buku
    id_cari = input("\nSilakan masukkan ID / Judul buku yang ingin anda cari: ")
    buku_ada = False # Menyimpan informasi apakah buku ada atau tidak ada

    # Mencari buku berdasarkan ID atau Judul
    for id_buku, buku in perpus.items():
        if id_cari == id_buku or id_cari.lower() == buku['judul_buku'].lower(): # Memeriksa apakah buku tersebut ada berdasarkan ID atau Judul Buku
            print("\nBuku Ditemukan!")
            buku_ada = True # Buku sudah ada
            
            # Menampilkan informasi buku yang dicari
            print(f"ID Buku: {id_buku}")
            print(f"Judul Buku: {buku['judul_buku']}")
            print(f"Penulis: {buku['penulis']}")
            print(f"Kategori: {buku['kategori']}\n")
    
    # Jika buku tidak ditemukan dalam daftar
    if not buku_ada: 
        print("Buku Anda Tidak Ditemukan\n") 

def tampilkan_buku(): # prosedur untuk menampilkan buku berdasarkan abjad judul buku yang terurut dari a - z
    if not perpus: # Memeriksa apakah daftar buku kosong
        print("\nDaftar Buku Masih Kosong\n")
        return # Kembali ke menu utama karena isi daftar buku masih kosong

    # Mengurutkan buku berdasarkan abjad judul buku
    buku_terurut = sorted(perpus.items(), key=lambda isi_buku: isi_buku[1]['judul_buku']) # mengakses value pertama di dictionary perpus, yakni judul buku

    print("\nDaftar Buku:")

    # Menampilkan semua buku yang ada dalam daftar terurut berdasarkan abjad judul buku
    for i, (id_buku, buku) in enumerate(buku_terurut, start=1):
        print(f"{i}. [{id_buku}] {buku['judul_buku']} - {buku['penulis']} (Kategori: {buku['kategori']})")
    print()

def hapus_buku(): # prosedur untuk menghapus buku
    if not perpus: # Memeriksa apakah daftar buku kosong
        print("\nDaftar Buku Masih Kosong\n")
        return # Kembali ke menu utama karena isi daftar buku masih kosong
    
    id_hapus = input("\nMasukkan ID Buku yang Ingin Anda Hapus: ") # Meminta ID Buku

    # Memeriksa apakah buku tersebut ada
    if id_hapus in perpus: 
        # jika ada
        del perpus[id_hapus] # Menghapus buku dari daftar
        print("\nBuku Telah Berhasil di Hapus\n")
        return # Kembali ke menu utama, karena telah berhasil menghapus buku
    
    print("\nBuku dengan ID tersebut tidak Ditemukan!\n") # Jika buku tidak ditemukan

def jumlah_buku_kategori(): # prosedur untuk menampilkan jumlah buku per kategori
    if not perpus: # Memeriksa apakah daftar buku kosong
        print("\nDaftar Buku Masih Kosong\n")
        return # Kembali ke menu utama karena isi daftar buku masih kosong

    print("\nJumlah Buku per Kategori:")
    hitung_kategori = {} # Dictionary untuk menyimpan jumlah buku per kategori

    for buku in perpus.values():
        # Menghitung jumlah buku per kategori
        hitung_kategori[buku['kategori']] = hitung_kategori.get(buku['kategori'], 0) + 1 

    # Menampilkan jumlah buku perkategori
    for i, (kategori, jumlah) in enumerate(hitung_kategori.items(), start=1):
        print(f"{i}. {kategori}: {jumlah} Buku")

def update_buku(): # prosedur untuk mengupdate isi informasi buku
    if not perpus: # Memeriksa apakah daftar buku kosong
        print("\nDaftar Buku Masih Kosong\n")
        return # Kembali ke menu utama karena isi daftar buku masih kosong

    # Lakukan perulangan sampai ID yang dimasukkan pengguna sudah benar
    while True:
        id_buku = input("\nMasukkan ID Buku Yang Ingin diganti: ") # Meminta pengguna untuk memasukkan ID Buku

        # Cek apakah buku dengan id tersebut ada
        if id_buku in perpus:
            # Jika ada
            print("Buku ditemukan!")

            # Meminta pengguna untuk memasukkan informasi buku
            judul_buku = input("Masukkan Judul Buku Baru: ")
            penulis = input("Masukkan Penulis Baru: ")
            kategori = input("Masukkan Kategori Baru: ")

            break # Keluar dari perulangan
        else:
            # jika buku belum ada maka minta pengguna untuk memasukkan ID Buku kembali
            print("Buku dengan ID Anda tidak Ditemukan, silahkan masukkan ID yang Benar!") # Jika ID tidak ada, maka minta pengguna untuk memasukkan kembali

    # Menyimpan informasi buku ke dalam dictionary dengan ID Buku sebagai Key
    perpus[id_buku] = {
        'judul_buku': judul_buku,
        'penulis': penulis,
        'kategori': kategori
    }

    print("\nBuku Berhasil Diupdate!\n")

def sistem_manajemen(): # prosedur untuk menu awal sistem perpustakaan

    # Menampilkan tampilan menu utama sampai pengguna memutuskan untuk
    # keluar dari program
    while True:
        # Menampilkan tampilan menu program
        print("\nSistem Manajemen Perpustakaan")
        print("1. Tambah Buku Baru")
        print("2. Cari Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Hapus Buku")
        print("5. Tampilkan Jumlah Buku per Kategori")
        print("6. Update Isi Buku")
        print("7. Keluar")

        # Meminta pengguna untuk memasukkan pilihan
        # sesuai dengan pilihan yang tertera
        pilihan = int(input("Masukkan Pilihan anda (1-7): "))

        # Mengecek kemudian Menjalankan prosedur sesuai pilihan pengguna
        if pilihan == 1:
            tambah_buku() # Masuk ke prosedur tambah buku
        elif pilihan == 2:
            cari_buku() # Masuk ke prosedur cari buku
        elif pilihan == 3:
            tampilkan_buku() # Masuk ke prosedur tampilkan buku
        elif pilihan == 4:
            hapus_buku() # Masuk ke prosedur hapus buku
        elif pilihan == 5:
            jumlah_buku_kategori() # Masuk ke prosedur jumlah buku per kategori
        elif pilihan == 6:
            update_buku() # Masuk ke prosedur update isi buku
        elif pilihan == 7:
            keluar = input("\nApakah anda yakin ingin keluar? (y/n): ").lower()

            # Cek pilihan pengguna apakah ingin keluar dari program atau tidak
            # Jika 'y' maka keluar, jika 'n' maka tidak
            if keluar == 'y':
                print("\nKeluar dari Sistem Manajemen Perpustakaan\n")
                break
            elif keluar == 'n':
                continue # Keluar dari program
        else:
            print("\nMasukkan Pilihan yang Benar!\n")

if __name__ == "__main__": # fungsi utama
    sistem_manajemen() # Masuk ke prosedur sistem manajemen
                       # Untuk menampilkan menu utama perpustakaan