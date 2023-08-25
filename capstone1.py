import pyinputplus as pyip

dataBuku = [
    {
        'id': 1001,
        'judul': 'Matematika',
        'penerbit': 'Karya Dunia',
        'harga': 45000,
        'qty': 25
    },
    {
        'id': 1002,
        'judul': 'Fisika',
        'penerbit': 'Erlangga',
        'harga': 60000,
        'qty': 30
    }
]

listMenu = [
            '1. Menampilkan Data Buku',
            '2. Menambahkan Data Buku',
            '3. Merubah Data Buku',
            '4. Menghapus Data Buku',
            '5. Exit Program',
            ]

recycle_bin = []

def generate_id_baru(x):
    sorted_ids = sorted([int(id) for id in x])
    
    for i in range(len(sorted_ids) + 1):
        if i + 1001 not in sorted_ids:
            return str(i + 1001)
        
def readData():
    inputRead = True
    while inputRead != '3':
        print('\n=====Data Buku=====\n')
        print('1. Menampilkan semua buku')
        print('2. Menampilkan salah satu buku')
        print('3. Urutkan data buku')
        print('4. Filter Data Buku')
        print('5. Kembali ke menu utama')
        inputRead = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-5) = ', min=1, max=5)

        if inputRead == 1:
            if len(dataBuku) != 0:
                print('\nDaftar Buku\n')
                print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                for i, buku in enumerate(dataBuku) :
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
            else:
                print('Buku tidak ditemukan')
            continue
        elif inputRead == 2:
            if len(dataBuku) != 0:
                inputCariBuku = pyip.inputInt(prompt='Masukkan ID buku (1001-1100) : ', min=1001, max=1100)

                print('\nID buku dengan nomor : {}'.format(inputCariBuku))
                for i, buku in enumerate(dataBuku) :
                    if str(buku['id']) == str(inputCariBuku):
                        print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                        print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
                        break  
                else:
                    print('Buku tidak ditemukan')
                        
            else:
                print('tidak ada list buku')
            continue
        elif inputRead == 3:
            sortOption = pyip.inputMenu(['Ascending', 'Descending'], numbered=True, prompt='\nSort data buku secara? \n').capitalize()
            sortColumn = pyip.inputMenu(['id', 'judul', 'penerbit', 'harga', 'qty'], numbered=True, prompt='Pilih kolom untuk mengurutkan: \n')

            if sortColumn in ['judul', 'penerbit']:
                sortedBooks = sorted(dataBuku, key=lambda x: x[sortColumn], reverse=(sortOption == 'Descending'))
            else:
                sortedBooks = sorted(dataBuku, key=lambda x: int(x[sortColumn]), reverse=(sortOption == 'Descending'))

            print('\nData Buku setelah diurutkan\n')
            print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
            for buku in sortedBooks:
                print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'], buku['judul'], buku['penerbit'], buku['harga'], buku['qty']))
        elif inputRead == 4:
            filterData()
        elif inputRead == 5:
            mainMenu()



def createData():
    inputCreate = True
    while inputCreate != '2':
        print('\n=====Tambah data Buku=====\n')
        print('1. Menambahkan data buku')
        print('2. kembali ke menu utama')
        inputCreate = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-2) = ', min=1, max=2)
        print('\n')
        if inputCreate == 1:
            inputid = pyip.inputInt(prompt='Masukkan ID buku (1001-1100) : ', min=1001, max=1100)
            existing_ids = [buku['id'] for buku in dataBuku]
            
            if int(inputid) in existing_ids:
                print('ID sudah digunakan. Mengenerate ID baru...')
                inputid = generate_id_baru(existing_ids)

                inputjudul = pyip.inputStr(prompt='Masukkan judul buku : ', ).title()
                inputpenerbit = pyip.inputStr(prompt='Masukkan penerbit buku : ').title()
                hargaBuku = pyip.inputInt(prompt='Masukkan harga buku : ', min=1)
                qtyBuku = pyip.inputInt(prompt='Masukkan quantity buku : ', min=1)
                save = True
                while save:
                    saveData = pyip.inputStr('Apa anda yakin data akan disimpan ? (Y/N) ').upper()
                    if saveData == 'Y':
                        data = {
                                    'id': inputid,
                                    'judul': inputjudul,
                                    'penerbit': inputpenerbit,
                                    'harga': hargaBuku,
                                    'qty': qtyBuku
                                }
                        dataBuku.append(data)
                        print('Data tersimpan')
                        save = False
                        break
                    elif saveData == 'N':
                        print('Data tidak tersimpan')
                        save = False
                        break
                    else:
                        print('Keyword yang anda masukkan salah')
            elif str(inputid) not in existing_ids:
                inputjudul = pyip.inputStr(prompt='Masukkan judul buku : ', ).title()
                inputpenerbit = pyip.inputStr(prompt='Masukkan penerbit buku : ').title()
                hargaBuku = pyip.inputInt(prompt='Masukkan harga buku : ', min=1)
                qtyBuku = pyip.inputInt(prompt='Masukkan quantity buku : ', min=1)
                save = True
                while save:
                    saveData = pyip.inputStr('Apa anda yakin data akan disimpan ? (Y/N) ').upper()
                    if saveData == 'Y':
                        data = {
                                    'id': inputid,
                                    'judul': inputjudul,
                                    'penerbit': inputpenerbit,
                                    'harga': hargaBuku,
                                    'qty': qtyBuku
                                }
                        dataBuku.append(data)
                        print('Data tersimpan')
                        save = False
                        break
                    elif saveData == 'N':
                        print('Data tidak tersimpan')
                        save = False
                        break
                    else:
                        print('Keyword yang anda masukkan salah')
        elif inputCreate == 2:
            mainMenu()              
 
def updateData():
    inputUpdate = True
    while inputUpdate != '2':
        print('\n=====Update data Buku=====\n')
        print('1. Merubah data buku')
        print('2. kembali ke menu utama')
        inputUpdate = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-2) = ', min=1, max=2)
        if inputUpdate == 1:
            if len(dataBuku) != 0:
                print('\nDaftar Buku\n')
                print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                for i, buku in enumerate(dataBuku):
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'], buku['judul'], buku['penerbit'], buku['harga'], buku['qty']))
            else:
                print('Buku tidak ditemukan')
            inputCariID = pyip.inputInt(prompt='\nMasukkan ID buku yang ingin dirubah (1001-1100) : ', min=1001, max=1100)
            for buku in dataBuku:
                if str(buku['id']) == str(inputCariID):
                    print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'], buku['judul'], buku['penerbit'], buku['harga'], buku['qty']))
                    lanjutUpdate = True
                    while lanjutUpdate:
                        inputLanjutUpdate = pyip.inputStr('\nApa anda yakin untuk melanjutkan update ? (Y/N) ').upper()
                        if inputLanjutUpdate == 'Y':
                            print("Kolom yang bisa diubah: Judul, Penerbit, Harga, Qty")
                            inputUpdateKolom = pyip.inputMenu(['Judul', 'Penerbit', 'Harga', 'Qty'], numbered=True, prompt='Masukkan kolom data yang ingin anda ubah ?  \n').lower()
                            if inputUpdateKolom in ['judul', 'penerbit', 'harga', 'qty']:
                                updateDataBaru = pyip.inputStr(f'Masukkan {inputUpdateKolom} yang baru = ').title()
                                buku[inputUpdateKolom] = updateDataBaru
                                print('Data berhasil diubah')
                            elif inputUpdateKolom in ['id']:
                                print('ID tidak bisa diubah')
                            else:
                                print('Kolom yang dimasukkan tidak valid')
                            lanjutUpdate = False
                        elif inputLanjutUpdate == 'N':
                            print('Data tidak berhasil diubah')
                            lanjutUpdate = False
                        else:
                            continue
                    break
            else:
                print('Data yang dicari tidak ditemukan')
        elif inputUpdate == 2:
            mainMenu()

def deleteData():
    inputDelete = True
    while inputDelete != '2':
        print('\n=====Delete data Buku=====\n')
        print('1. Hapus data buku')
        print('2. Restore data dari Recycle Bin')
        print('3. Kembali ke menu utama')
        inputDelete = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-3) = ', min=1, max=3)
        if inputDelete == 1:
            if len(dataBuku) != 0:
                print('\nDaftar Buku\n')
                print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                for i, buku in enumerate(dataBuku) :
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
            else:
                print('Buku tidak ditemukan')
            inputCariID = pyip.inputInt(prompt='\nMasukkan ID buku yang ingin dihapus (1001-1100) : ', min=1001, max=1100)
            for buku in dataBuku:
                if str(buku['id']) == str(inputCariID):
                    hapusBuku = True
                    while hapusBuku:
                        inputHapus = pyip.inputStr('Apa anda yakin untuk menghapus data ? (Y/N) ').upper()
                        if inputHapus == 'Y':
                            idx = dataBuku.index(buku)
                            deletedItem = dataBuku.pop(idx)
                            recycle_bin.append(deletedItem)
                            print('Data sudah dipindahkan ke recycle bin')
                            hapusBuku = False
                            break
                        elif inputHapus == 'N':
                            print('Data gagal terhapus')
                            hapusBuku = False
                            break
                        else:
                            print('Keyword yang anda masukkan salah')
                    break
                else:
                    continue
            else:
                print('Data yang dicari tidak ditemukan')
        elif inputDelete == 2:
            restoreData()
        elif inputDelete == 3:
            mainMenu()

def restoreData():
    inputRestore = True
    while inputRestore != '2':
        print('\n=====Restore data dari Recycle Bin=====')
        print('1. Restore data buku')
        print('2. Kembali ke menu utama')
        inputRestore = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-2) = ', min=1, max=2)
        if inputRestore == 1:
            if len(recycle_bin) != 0:
                print('\nDaftar Buku\n')
                print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                for i, buku in enumerate(recycle_bin) :
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
            else:
                print('Buku tidak ditemukan')
            if len(recycle_bin) != 0:
                inputRestoreID = pyip.inputInt(prompt='Masukkan ID buku yang ingin direstore : ')
                for buku in recycle_bin:
                    if str(buku['id']) == str(inputRestoreID):
                        restoreBuku = True
                        while restoreBuku:
                            inputRestore = pyip.inputStr('Apa anda yakin untuk merestore data ? (Y/N) ').upper()
                            if inputRestore == 'Y':
                                idx = recycle_bin.index(buku)
                                restoredItem = recycle_bin.pop(idx)
                                dataBuku.append(restoredItem)
                                print('Data berhasil direstore')
                                restoreBuku = False
                                break
                            elif inputRestore == 'N':
                                print('Data gagal direstore')
                                restoreBuku = False
                                break
                            else:
                                print('Keyword yang anda masukkan salah')
                        break
                else:
                    print('Data yang dicari tidak ditemukan di Recycle Bin')
            else:
                print('Recycle Bin kosong')
        elif inputRestore == 2:
            mainMenu()

def filterData(filteredBooks=None):
    print('\n=====Filter Data Buku=====\n')
    print('1. Filter berdasarkan Judul')
    print('2. Filter berdasarkan Harga')
    print('3. Filter berdasarkan Penerbit')
    print('4. Kembali ke menu menampilkan data buku')
    filterOption = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-4) = ', min=1, max=4)
    
    if filterOption == 1:
        filterJudul = pyip.inputStr(prompt='Masukkan judul buku yang ingin difilter: ').title()
        filteredBooks = [
            buku for buku in dataBuku 
            if filterJudul in buku['judul']]
    elif filterOption == 2:
        if filteredBooks is None:
            filteredBooks = filterHarga()
    elif filterOption == 3:
        filterPenerbit = pyip.inputStr(prompt='Masukkan penerbit buku yang ingin difilter: ').title()
        filteredBooks = [
            buku for buku in dataBuku 
            if filterPenerbit in buku['penerbit']]
    elif filterOption == 4:
        readData()
    else:
        print('Opsi yang dimasukkan tidak valid')

    if len(filteredBooks) > 0:
        print('\nData Buku setelah difilter\n')
        print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
        for buku in filteredBooks:
            print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'], buku['judul'], buku['penerbit'], buku['harga'], buku['qty']))
    else:
        print('\nTidak ada data yang cocok dengan filter')

def filterHarga():
    print('\n=====Filter Harga Buku=====\n')
    print('1. Filter Harga Lebih Besar Dari')
    print('2. Filter Harga Lebih Kecil Dari')
    print('3. Kembali ke menu filter data')
    filterOption = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-3) = ', min=1, max=3)

    filteredBooks = []  # filteredBooks sebagai list kosong

    if filterOption == 1:
        hargaThreshold = pyip.inputInt(prompt='Masukkan harga minimal: ')
        filteredBooks = [
            buku for buku in dataBuku 
            if buku['harga'] > hargaThreshold]
    elif filterOption == 2:
        hargaThreshold = pyip.inputInt(prompt='Masukkan harga maksimal: ')
        filteredBooks = [
            buku for buku in dataBuku 
            if buku['harga'] < hargaThreshold]
    elif filterOption == 3:
        filterData()
    else:
        print('Opsi yang dimasukkan tidak valid')

    return filteredBooks

def mainMenu():
    menu = True
    while menu != '5':
        print('\n=====Aplikasi penjualan barang toko Buku Multimedia=====\n')
        for i in listMenu:
            print(i)
        menu = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-5) = ', min=1, max=5)
        if(menu == 1) :
            readData()
        elif(menu == 2) :
            createData()
        elif(menu == 3) :
            updateData()
        elif(menu == 4) :
            deleteData()
        elif(menu == 5) :
            print('Terima Kasih')
            quit()
        else:
            print('Angka yang diketik salah')

mainMenu()