import os
import sys

pilih=0
dataSiswa=[]
namaFile = "Data_Mahasiswa.txt"

class ListMahasiswa:
    def __init__(self, nama,nim, jurusan, angkatan, data_vaksin):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.angkatan = angkatan
        self.data_vaksin = data_vaksin

    def getNama(self):
        return self.nama
    def getNim(self):
        return self.nim
    def getJurusan(self):
        return self.jurusan
    def getAngkatan(self):
        return self.angkatan
    def getDataVaksin(self):
        return self.data_vaksin

    def setNama(self, nama):
        self.nama = nama
    def setNim(self, nim):
        self.nim = nim
    def setJurusan(self, jurusan):
        self.jurusan = jurusan
    def setAngkatan(self, angkatan):
        self.nim = angkatan
    def setDataVaksin(self, data_vaksin):
        self.nim = data_vaksin

def readFileToList():
     # read file to list
    with open(namaFile, 'r') as file:
        fileSiswa = file.readlines()
        fileSiswa = [x.rstrip() for x in fileSiswa]
        
    print(12*'-')

    if not dataSiswa :
        for listSiswa in fileSiswa :
            splitSiswa = listSiswa.split(';')
            print(f"Nama\t\t{splitSiswa[0]}\nNim\t\t{splitSiswa[1]}\nJurusan\t\t{splitSiswa[2]}\nAngkatan\t{splitSiswa[3]}\nData Vaksin\t{splitSiswa[4]}\n")
            mahasiswa = ListMahasiswa(splitSiswa[0], splitSiswa[1], splitSiswa[2], splitSiswa[3], splitSiswa[4])
            dataSiswa.append(mahasiswa)
    else :
        for listSiswa in fileSiswa :
            splitSiswa = listSiswa.split(';')
            print(f"Nama\t\t{splitSiswa[0]}\nNim\t\t{splitSiswa[1]}\nJurusan\t\t{splitSiswa[2]}\nAngkatan\t{splitSiswa[3]}\nData Vaksin\t{splitSiswa[4]}\n")

# Menu
def menu():
    os.system("cls")

    print("Data Vaksin Mahasiswa SV IPB UNIVERSITY")
    print("-------------------------------------------")
    print("1. Input Data Vaksin Mahasiwa")
    print("2. Tampilkan Data Vaksin Mahasiswa")
    print("3. Update Data Vaksin Mahasiswa")
    print("4. Delete Data Vaksin Mahasiswa")
    print("5. Informasi Pengembang")
    print("6. Log Out")
    pilih = int(input("Masukkan Pilihan Anda : ")+' ')
    if pilih == 1 :
        pilih1()
        menu()

# Tampilkan Data Vaksin Mahasiswa
    elif pilih == 2 :
        os.system("cls")
        print("Data Vaksin Mahasiswa")
        readFileToList()        
        print("----------------------")
        input("Press Enter, Untuk Kembali Ke Menu Utama")
        menu()
    
# Isi Data Vaksin Mahasiswa
    elif pilih == 3 :
        readFileToList()
        index_update    = int(input("Masukkan pilihan index     :"))-1
        nama            = input("Masukkan nama baru         :")
        nim             = input("Masukkan nim baru          :")
        jurusan         = input("Masukkan jurusan baru      :")
        angkatan        = int(input("Masukkan angkatan baru     :"))
        data_vaksin     = input("Masukkan data vaksin baru  :")
        # Update data
        dataSiswa[index_update].setNama(nama)
        dataSiswa[index_update].setNim(nim)
        dataSiswa[index_update].setJurusan(jurusan)
        dataSiswa[index_update].setAngkatan(angkatan)
        dataSiswa[index_update].setDataVaksin(data_vaksin)
        # Hapus file txt
        if os.path.exists(namaFile):
            os.remove(namaFile)
        else:
            print("The file does not exist")#add this to prevent errors
        # Write ke txt
        with open(namaFile, 'w') as filehandle:
            for objMahasiswa in dataSiswa:
                teks = f"{objMahasiswa.getNama()};{objMahasiswa.getNim()};{objMahasiswa.getJurusan()};{objMahasiswa.getAngkatan()};{objMahasiswa.getDataVaksin()}\n"
                filehandle.write(teks)
            filehandle.close()

        input("Press Enter, Untuk Kembali Ke Menu Utama")
        menu()

# Delete Data Siswa
    elif pilih == 4:
        readFileToList()

        index_delete = int(input("Masukkan index yang akan dihapus : "))-1
        if (dataSiswa[index_delete]):
            del dataSiswa[index_delete]
            # delete txt
            if os.path.exists(namaFile):
                os.remove(namaFile)
            else:
                print("The file does not exist")
            # write txt baru
            with open(namaFile, 'w') as filehandle:
                for objMahasiswa in dataSiswa:
                    teks = f"{objMahasiswa.getNama()};{objMahasiswa.getNim()};{objMahasiswa.getJurusan()};{objMahasiswa.getAngkatan()};{objMahasiswa.getDataVaksin()}\n"
                    filehandle.write(teks)
                filehandle.close()
            print("Data berhasil dihapus")
        menu()

# Developer Program
    elif pilih == 5 :
        developer()
        input("\n\n Press Enter, Untuk Kembali Ke Menu Utama")
        menu()

# Logout
    elif pilih == 6 :
        sys.exit()

# Developer
def developer():
    os.system("cls")
    print("SV IPB UNIVERSITY | Teknologi Rekayasa Komputer 59 B1")
    print("-----------------------------------------------------")
    print("Raihan Hammam Salsabil               | J0404221127")
    print("Surya Angga                          | J0404221089")
    print("Putri Salsabila                      | J0404221169")
    print("Hexania Nurul Rizkia Putri           | J0404221042")
    print("Alfisyahrin Denzel Shaquille Beryl   | J0404221098")
    print("-----------------------------------------------------")

# Fungsi nput
def pilih1():
    ulang = "Y"
    while ulang in("y", "Y"):
        os.system("cls")
        print("Input Data Vaksin Mahasiswa")
        nama        = input("Nama                   : ")
        nim         = input("NIM                    : ")
        jurusan     = input("Jurusan                : ")
        angkatan    = int(input("Angkatan              : "))
        dataVaksin  = input("Data Vaksin            : ")
        mahasiswa   = ListMahasiswa(nama, nim, jurusan, angkatan, dataVaksin)

        file_bio = open("Data_Mahasiswa.txt", "a")
        teks = f"{mahasiswa.getNama()};{mahasiswa.getNim()};{mahasiswa.getJurusan()};{mahasiswa.getAngkatan()};{mahasiswa.getDataVaksin()}\n"

        file_bio.write(teks)
        file_bio.close()
        dataSiswa.clear()
        ulang = input("Apakah Anda Ingin Menginput Data Lagi ? (Y/T) ")
menu()