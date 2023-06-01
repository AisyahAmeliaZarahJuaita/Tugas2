class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NPM: ", self.npm)
        print("Prodi: ", self.prodi.NamaProdi)


class Prodi:
    def __init__(self, nama_prodi):
        self.NamaProdi = nama_prodi
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Prodi", self.NamaProdi)
        for mahasiswa in self.DaftarMahasiswa:
            print(mahasiswa.nama)
            print(mahasiswa.npm)
            
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarProdi = []
    
    def tambah_prodi(self, prodi):
        self.DaftarProdi.append(prodi)
    
    def tampilkan_daftar_prodi(self):
        print("Daftar Prodi di Universitas", self.NamaUniversitas)
        for prodi in self.DaftarProdi:
            print(prodi.NamaProdi)

# 1. Mengimplementasikan sebuah kelas Mahasiswa, Prodi, dan Universitas yang ada di dalam program 

# 2. Membuat sebuah objek pada Universitas dengan nama "Bengkulu University"
universitas = Universitas("Bengkulu University")

# 3. Membuat sebuah objek yang ada pada Prodi dengan nama "Teknik Informatika" dan tambahkan ke dalam Bengkulu Universitas 
teknik_informatika = Prodi("Teknik Informatika")
universitas.tambah_prodi(teknik_informatika)

# 4. Membuat sebuah objek yang ada Prodi dengan nama "Teknik Sipil" dan tambahkan ke dalam Bengkulu Universitas 
teknik_sipil = Prodi("Teknik Sipil")
universitas.tambah_prodi(teknik_sipil)

# 5. Membuat sebuah objek yang ada Prodi dengan nama "Teknik Elektro" dan tambahkan ke dalam Bengkulu Universitas
teknik_elektro = Prodi("Teknik Elektro")
universitas.tambah_prodi(teknik_elektro)

# 6. Membuat sebuah objek yang ada Prodi dengan nama "Teknik Mesin" dan tambahkan ke dalam Bengkulu Universitas
teknik_mesin = Prodi("Teknik Mesin")
universitas.tambah_prodi(teknik_mesin)

# 7. Membuat sebuah objek yang ada Prodi dengan nama "Teknik Arsitektur" dan tambahkan ke dalam Bengkulu Universitas 
teknik_arsitektur = Prodi("Teknik Arsitektur")
universitas.tambah_prodi(teknik_arsitektur)

# 8. Membuat sebuah objek yang ada Prodi dengan nama "Sistem Informasi" dan tambahkan ke dalam Bengkulu Universitas 
sistem_informasi = Prodi("Sistem Informasi")
universitas.tambah_prodi(sistem_informasi)

mahasiswa1 = Mahasiswa("Aisyah Amelia Zarah Juaita", "G1A022075", teknik_informatika)
teknik_informatika.tambah_mahasiswa(mahasiswa1)

mahasiswa2 = Mahasiswa("Amelia Salsabillah", "G1B022016", teknik_sipil)
teknik_sipil.tambah_mahasiswa(mahasiswa2)

mahasiswa3 = Mahasiswa("Setiawan Aprizal", "G1D022080", teknik_elektro)
teknik_elektro.tambah_mahasiswa(mahasiswa3)

mahasiswa4 = Mahasiswa("Tomi Putra", "G1C022020", teknik_mesin)
teknik_mesin.tambah_mahasiswa(mahasiswa4)

mahasiswa5 = Mahasiswa("Nadia Gumanta", "G1E022025", teknik_arsitektur)
teknik_arsitektur.tambah_mahasiswa(mahasiswa5)

mahasiswa6 = Mahasiswa("Ikram Muhammad", "G1F022016", sistem_informasi)
sistem_informasi.tambah_mahasiswa(mahasiswa6)

teknik_informatika.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()

teknik_sipil.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()

teknik_elektro.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()

teknik_mesin.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()

teknik_arsitektur.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()

sistem_informasi.tampilkan_daftar_mahasiswa()
universitas.tampilkan_daftar_prodi()










