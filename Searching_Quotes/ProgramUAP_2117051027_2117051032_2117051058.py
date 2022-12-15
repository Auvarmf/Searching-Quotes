import developers
import json
import requests
import time  # waktu
import datetime  # tanggal
import os

katabijak = requests.get(
    'https://katanime.vercel.app/api/getbyanime?anime=naruto&page=1')
katabijak2 = requests.get(
    'https://katanime.vercel.app/api/getbyanime?anime=bleach&page=1')

katabijak
katabijak2

katabijak = katabijak.json()
katabijak2 = katabijak2.json()

katabijak['result']
katabijak2['result']


def alldata():
    print('----------NARUTO----------')
    for data in katabijak['result']:
        print('Character\t :', data['character'].upper(),
              '\nQuotes\t\t :', data['indo'], '\n')

        print('----------BLEACH----------')
    for data in katabijak2['result']:

        print('Character\t :', data['character'].upper(),
              '\nQuotes\t\t :', data['indo'], '\n')


def characterlist(nama):
    if nama == 1:
        print('\nHatake Kakashi')
        for data in katabijak['result']:
            if data['character'] == 'Hatake Kakashi':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict["Hatake Kakashi"])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 2:
        print('\nRock Lee')
        for data in katabijak['result']:
            if data['character'] == 'Rock Lee':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Rock Lee'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 3:
        print('\nGaara')
        for data in katabijak['result']:
            if data['character'] == 'Gaara':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Gaara'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 4:
        print('\nNaruto Uzumaki')
        for data in katabijak['result']:
            if data['character'] == 'Naruto Uzumaki':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Naruto Uzumaki'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 5:
        print('\nHaku')
        for data in katabijak['result']:
            if data['character'] == 'Haku':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Haku'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 6:
        print('\nObito Uchiha')
        for data in katabijak['result']:
            if data['character'] == 'Obito Uchiha':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Obito Uchiha'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 7:
        print('\nItachi Uchiha')
        for data in katabijak['result']:
            if data['character'] == 'Itachi Uchiha':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Itachi Uchiha'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama == 8:
        print('\nNara Shikamaru')
        for data in katabijak['result']:
            if data['character'] == 'Nara Shikamaru':
                print('Quotes\t :', data['indo'])
        print()
        print(narutoDict['Nara Shikamaru'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    else:
        print('\nPilihan Tidak Tersedia!')

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()


def characterlist2(nama2):

    if nama2 == 1:
        print('\nKurosaki Ichigo')
        for data in katabijak2['result']:
            if data['character'] == 'Kurosaki Ichigo':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Kurosaki Ichigo'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama2 == 2:
        print('\nAbarai Renji')
        for data in katabijak2['result']:
            if data['character'] == 'Abarai Renji':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Abarai Renji'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama2 == 3:
        print('\nKuchiki Byakuya')
        for data in katabijak2['result']:
            if data['character'] == 'Kuchiki Byakuya':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Kuchiki Byakuya'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

    elif nama2 == 4:
        print('\nAizen Sousuke')
        for data in katabijak2['result']:
            if data['character'] == 'Aizen Sousuke':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Aizen Sousuke'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

        elif nama2 == 5:
            print('\nZaraki Kenpachi')
    for data in katabijak2['result']:
        if data['character'] == 'Zaraki Kenpachi':
            print('Quotes\t :', data['indo'])
            print()
            print(bleachDict['Zaraki Kenpachi'])

            print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

        elif nama2 == 6:
            print('\nUrahara Kisuke')
        for data in katabijak2['result']:
            if data['character'] == 'Urahara Kisuke':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Urahara Kisuke'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

        elif nama2 == 7:
            print('\nUlquiorra Schiffer')
        for data in katabijak2['result']:
            if data['character'] == 'Ulquiorra Schiffer':
                print('Quotes\t :', data['indo'])
        print()
        print(bleachDict['Ulquiorra Schiffer'])

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()

        else:
            print('\nPilihan Tidak Tersedia!')

        print()
        balik = input("\nBack to menu(y/n)? ")
        if balik == 'y' or 'Y':
            os.system('cls')
            main_menu()


narutoDict = {
    "Hatake Kakashi": "Data diri : \n" +
    "Kakashi Hatake (派竹 歌々子, Hatake Kakashi) adalah shinobi Konohagakure dari klan Hatake.\n" +
    "Terkenal sebagai Kakashi si Sharingan (写輪眼のカカシ, Sharingan no Kakashi), \n" +
    "dia adalah salah satu ninja Konoha yang paling berbakat; secara teratur tampak suka memberi nasihat \n" +
    "dan berkepemimpinan meskipun dia tidak menyukai tanggung jawab pribadi. Untuk murid-muridnya di Tim 7, \n" +
    "Kakashi mengajarkan pentingnya kerja sama tim, sebuah pelajaran yang dia terima, bersama dengan Sharingan, \n" +
    "dari teman masa kecilnya, Obito Uchiha. Setelah Perang Dunia Shinobi Keempat, Kakashi menjadi Hokage Keenam \n" +
    "(六代目火影, Rokudaime Hokage; Secara harfiah berarti Bayangan Api Keenam).\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Kakashi_Hatake\n",
    "Rock Lee": "Data diri : \n" +
    "Rock Lee (ロック・リー, Rokku Rī) adalah shinobi dari Konohagakure. Sementara ia tidak memiliki keterampilan tertentu \n" +
    "biasanya terkait dengan kehidupan sebagai seorang ninja, Lee berusaha untuk menebus kekurangannya dengan cara apa pun \n" +
    "yang dia bisa. Sebagai anggota Tim Guy, ia menerima pelatihan khusus dalam hal ini dari gurunya, Might Guy, \n" +
    "untuk menjadi seorang ahli taijutsu.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Rock_Lee\n",

    "Gaara": "Data diri : \n" +
    "Gaara (我愛羅, Gaara) adalah shinobi dari Sunagakure. Shukaku disegel ke dalam tubuhnya pada hari ia dilahirkan, \n" +
    "prosedur yang menyebabkan kematian ibunya. Dianggap sebagai monster oleh desa dan dengan tidak ada yang mencintainya, \n" +
    "Gaara menjadi benci pada dunia dan mulai hanya mengandalkan kekuatannya sendiri, dengan mendapatkan gelar \n" +
    "Gaara Sang Pasir Terjun (砂瀑の我愛羅).\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Gaara\n",
    "Naruto Uzumaki": "Data diri : \n" +
    "Naruto Uzumaki (渦巻 鳴門, Uzumaki Naruto) adalah shinobi dari Konohagakure. Dia menjadi jinchūriki dari Ekor Sembilan \n" +
    "pada hari kelahirannya — sebuah nasib yang menyebabkan dia dijauhi oleh sebagian besar penduduk Konoha sepanjang masa kecilnya. \n" +
    "Setelah bergabung dengan Tim Kakashi, Naruto bekerja keras untuk mendapatkan pengakuan desa sambil mengejar mimpinya \n" +
    "untuk menjadi Hokage.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Naruto_Uzumaki\n",
    "Haku": "Data diri : \n" +
    "Haku (白, Haku) dalah seorang yatim piatu dari Negara Air, dan keturunan klan Yuki. \n" +
    "Ia kemudian menjadi shinobi setelah bertemu Zabuza Momochi yang menjadi mitranya, dan akhirnya menjadi Ninja Bayaran.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Haku\n",
    "Obito Uchiha": "Data diri : \n" +
    "Obito Uchiha (うちはオビト, Uchiha Obito) adalah anggota klan Uchiha dari Konohagakure. Dia diyakini telah meninggal selama Perang \n" +
    "Dunia Shinobi Ketiga, satu-satunya warisan yang masih ada adalah Sharingan yang dia berikan kepada rekan setimnya, Kakashi Hatake.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Obito_Uchiha\n",
    "Itachi Uchiha": "Data diri : \n" +
    "Itachi Uchiha (団扇 鼬, Uchiha Itachi) adalah seorang anak ajaib klan Uchiha dari Konohagakure. \n" +
    "Ia menjadi seorang penjahat internasional setelah membunuh seluruh klan, dan hanya menyelamatkan adiknya, Sasuke.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Itachi_Uchiha\n",
    "Nara Shikamaru": "Data Diri : \n" +
    "Shikamaru Nara (奈良シカマル, Nara Shikamaru) adalah anggota Klan Nara dari Konohagakure. Meskipun malas adalah sifat alaminya, \n" +
    "Shikamaru memiliki kecerdasan langka dan konsisten yang memungkinkan dia untuk menang dalam pertempuran.\n" +
    "\nLink Fandom : https://naruto.fandom.com/id/wiki/Shikamaru_Nara\n"

}


bleachDict = {
    "Kurosaki Ichigo": "Data diri : \n" +
    "Ichigo Kurosaki (黒崎 一護, Kurosaki Ichigo) adalah seorang Manusia yang memiliki kekuatan Shinigami. Dia juga adalah seorang \n" +
    "Shinigami Pengganti. Ichigo adalah anak dari Isshin dan Masaki Kurosaki, dan kakak tertua dari Karin dan Yuzu. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Ichigo_Kurosaki\n",
    "Abarai Renji": "Data diri : \n" +
    "Renji Abarai (阿散井 恋次, Abarai Renji) adalah letnan Divisi 6 dibawah pimpinan Kapten Byakuya Kuchiki. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Renji_Abarai\n",
    "Kuchiki Byakuya": "Data diri : \n" +
    "Byakuya Kuchiki (朽木 白哉, Kuchiki Byakuya) adalah kepala ke-28 Keluarga Kuchiki, satu dari empat keluarga bangsawan \n" +
    "di Soul Society. Dia juga adalah kapten dari Divisi 6 di Gotei 13 dengan letnan Renji Abarai. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Byakuya_Kuchiki\n",
    "Aizen Sousuke": "Data diri : \n" +
    "Sōsuke Aizen (藍染 惣右介, Aizen Sōsuke) adalah mantan kapten Divisi 5 di Gotei 13. Sebelum dia meninggalkan Soul Society " +
    "bersama pengikutnya, Gin Ichimaru dan Kaname Tōsen. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Sōsuke_Aizen\n",
    "Zaraki Kenpachi": "Data diri : \n" +
    "Kenpachi Zaraki (更木 剣八, Zaraki Kenpachi) adalah Kapten yang sedang memimpin Divisi 11 di Gotei 13. \n" +
    "Dia adalah Kenpachi kesebelas, Letnannya adalah Yachiru Kusajishi. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Kenpachi_Zaraki\n",
    "Urahara Kisuke": "Data diri : \n" +
    "Kisuke Urahara (浦原 喜助, Urahara Kisuke) adalah mantan kapten Divisi 12, sekaligus pendiri dari \n" +
    "Institut Penelitian dan Pengembangan Shinigami.\n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Kisuke_Urahara\n",
    "Ulquiorra Schiffer": "Data diri : \n" +
    "Ulquiora Cifer (ウルキオラ・シファー, Urukiora Shifā)[2] adalah Cuatro Espada (nomor 4) di pasukan Arrancar Sōsuke Aizen. \n" +
    "\nLink Fandom : https://bleach.fandom.com/id/wiki/Ulquiorra_Cifer\n"
}


def feedback():
    pilihan = 0
    print("-----Pilihan File Feedback------\nRequestAnime.txt atau KritikSaran.txt")
    nama_file = input("\nMasukkan nama file (.txt) :")
    while pilihan != 3:
        while (True):
            try:
                print("\n1 : Membuka", nama_file, " \n2 : Menambah",
                      nama_file, " \n3 : Keluar Program")
                pilihan = int(input("Pilihan : "))
                if pilihan <= 0 or pilihan > 3:
                    raise ValueError
                print("")
                break
            except:
                print("Masukkan Pilihan 1, 2, 3! BUKAN HURUF ATAU KATA!!!\n")

        if pilihan == 1:
            try:
                infile = open(nama_file, "r")
                print("\nIsi dari", nama_file, ":", infile.read())
                infile.close()
            except FileNotFoundError:
                print("File", nama_file, "Tidak ada")

        elif pilihan == 2:
            try:
                with open(nama_file, 'r') as nf:
                    print("\nIsi dari", nama_file, ": ")
                    print(nf.read())
                isi = input("\nTambahkan teks ke file : ")
                outfile = open(nama_file, 'a')
                outfile.write("\n")
                outfile.write(isi)
                outfile = open(nama_file, 'r')
                print("NOTIFIKASI : ", isi,
                      "Berhasil ditambahkan pada File", nama_file, "\n")
                print("\nIsi dari", nama_file, ":", outfile.read())
                outfile.close()
            except FileNotFoundError:
                print("File", nama_file, "Tidak ada")


developers.pengembang()

waktu = datetime.datetime.now()
for i in range(3):
    nama = input("Masukkan Nama Anda : ")
    print("")
    print("NOTIFIKASI !!! | Waktu  : ", str(waktu))
    print("Selamat Datang " + nama)
    time.sleep(2)
    break
  
  
def main_menu():
    print('\n<<----- Selamat datang di kumpulan quotes anime ----->>\n')
    print('Menu\n1.Tampilkan semua quotes\n2.Cari quotes berdasarkan karakter\n3.Feedback')

    while True:
        try:
            menu = int(input("\nPilih menu : "))
            print()
            break
        except:
            print('Inputan salah!')

    if menu == 1:
        alldata()

    elif menu == 2:
        listAnime = ["1. Naruto", "2. Bleach"]
        for i in range(2):
            print(listAnime[i])

        menu2 = int(input("\nPilih Anime : "))
        print()

        if menu2 == 1:
            Karakter = ["1. Hatake Kakashi",
                        "2. Rock Lee",
                        "3. Gaara",
                        "4. Naruto Uzumaki",
                        "5. Haku",
                        "6. Obito Uchiha",
                        "7. Itachi Uchiha",
                        "8. Nara Shikamaru"]
            for i in range(8):
                print(Karakter[i])

            name = int(input("\nPilih Karakter : \n"))
            characterlist(name)

        elif menu2 == 2:
            Karakter2 = ["1. Kurosaki Ichigo",
                         "2. Abarai Renji",
                         "3. Kuchiki Byakuya",
                         "4. Aizen Sousuke",
                         "5. Zaraki Kenpachi",
                         "6. Urahara Kisuke",
                         "7. Ulquiorra Schiffer"]

            for i in range(7):
                print(Karakter2[i])
            name2 = int(input("\nPilih Karakter : "))
            characterlist2(name2)
        else:
            print("\nMenu tidak tersedia")
    elif menu == 3:
        feedback()
    else:
        print('\nPilihan Tidak Tersedia!')
main_menu()