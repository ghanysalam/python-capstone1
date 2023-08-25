# def deleteData():
#     inputDelete = True
#     while inputDelete != '2':
#         print('Delete data Buku')
#         print('1. Hapus data buku')
#         print('2. kembali ke menu utama')
#         inputDelete = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-2) = ', min=1, max=2)
#         if inputDelete == 1:
#             inputCariID = pyip.inputInt(prompt='Masukkan ID buku yang ingin dihapus (1001-1999) : ', min=1001, max=1100)
#             for buku in listBuku:
#                 if buku['idBuku'] == str(inputCariID):
#                     hapusBuku = True
#                     while hapusBuku:
#                         inputHapus = pyip.inputStr('Apa anda yakin untuk menghapus data ? (Y/N) ').upper()
#                         if inputHapus == 'Y':
#                             idx = listBuku.index(buku)
#                             listBuku.pop(idx)
#                             print('Data sudah terhapus')
#                             hapusBuku = False
#                             break
#                         elif inputHapus == 'N':
#                             print('Data gagal terhapus')
#                             hapusBuku = False
#                             break
#                         else:
#                             print('Keyword yang anda masukkan salah')
#                     break
#                 else:
#                     continue
#             else:
#                 print('Data yang dicari tidak ditemukan')
#         elif inputDelete == 2:
#             mainMenu()


if inputRestore == 'Y':
    idx = recycle_bin.index(buku)
    restored_item = recycle_bin.pop(idx)
    listBuku.append(restored_item)
    print('Data berhasil direstore')
    restoreBuku = False
    break
else:
 

 if inputHapus == 'Y':
    idx = listBuku.index(buku)
    deleted_item = listBuku.pop(idx)
    recycle_bin.append(deleted_item)
    print('Data sudah dipindahkan ke recycle bin')
    hapusBuku = False
    break
else:

if inputUpdateKolom == 1:
                                updateDataBaru = pyip.inputStr(f'Masukkan ID buku yang baru = ')
                                lanjutUpdate = False
                                simpanDataUpdate = True
                                while simpanDataUpdate:
                                    inputLanjutUpdateData = pyip.inputStr('Apa anda yakin untuk merubah data ? (Y/N) ').upper()
                                    if inputLanjutUpdateData == 'Y':
                                        buku['idBuku'] = updateDataBaru
                                        print('Data berhasil diubah')
                                        simpanDataUpdate = False
                                    elif inputLanjutUpdateData == 'N':
                                        print('Data tidak berhasil diubah')
                                        simpanDataUpdate = False
                                    else:
                                        print('Keyword yang anda masukkan salah')

def updateData():
    inputUpdate = True
    while inputUpdate != '2':
        print('\n=====Update data Buku=====\n')
        print('1. Merubah data buku')
        print('2. kembali ke menu utama')
        inputUpdate = pyip.inputInt(prompt='Silahkan pilih opsi yang ingin dijalankan (1-2) = ', min=1, max=2)
        if inputUpdate == 1:
            if len(listBuku) != 0:
                print('\nDaftar Buku\n')
                print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                for i, buku in enumerate(listBuku) :
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
            else:
                print('Buku tidak ditemukan')
            inputCariID = pyip.inputInt(prompt='Masukkan ID buku yang ingin dirubah (1001-1100) : ', min=1001, max=1100)
            for buku in listBuku:
                if str(buku['id']) == str(inputCariID):
                    print('ID Buku\t\t| Judul Buku  \t\t| Penerbit Buku\t\t| Harga\t\t| Qty')
                    print('{}\t\t| {}  \t\t| {}\t\t| {}\t\t| {}'.format(buku['id'],buku['judul'],buku['penerbit'],buku['harga'],buku['qty']))
                    lanjutUpdate = True
                    while lanjutUpdate:
                        inputLanjutUpdate = pyip.inputStr('Apa anda yakin untuk melanjutkan update ? (Y/N) ').upper()
                        if inputLanjutUpdate == 'Y': 
                            inputUpdateKolom = pyip.inputStr('Masukkan kolom data yang ingin anda ubah ? (JUDUL / PENERBIT / HARGA / QTY) ', blockRegexes=[(r"[0-9]")]).lower()
                            updateDataBaru = pyip.inputStr(f'Masukkan {inputUpdateKolom} yang baru = ')
                            lanjutUpdate = False
                            simpanDataUpdate = True
                            while simpanDataUpdate:
                                inputLanjutUpdateData = pyip.inputStr('Apa anda yakin untuk merubah data ? (Y/N) ').upper()
                                if inputLanjutUpdateData == 'Y':
                                    buku[inputUpdateKolom] = updateDataBaru
                                    print('Data berhasil diubah')
                                    simpanDataUpdate = False
                                elif inputLanjutUpdateData == 'N':
                                    print('Data tidak berhasil diubah')
                                    simpanDataUpdate = False
                                else:
                                    print('Keyword yang anda masukkan salah')
                            break
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

            inputUpdateKolom = pyip.inputStr('Masukkan kolom data yang ingin anda ubah ? ').lower()