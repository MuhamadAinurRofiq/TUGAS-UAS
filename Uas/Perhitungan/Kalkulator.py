def kalkulator ():
    a=[]
    b=[]
    def jumlah (a,b):
        a=int(input('Masukkan nilai \t: '))
        b=int(input('Masukkan nilai \t: '))
        jumlah = a+b
        return jumlah
    def kurang (a,b):
        a=int(input('Masukkan nilai \t: '))
        b=int(input('Masukkan nilai \t: '))
        kurang = a-b  
        return kurang
    def kali (a,b):
        a=int(input('Masukkan nilai \t: '))
        b=int(input('Masukkan nilai \t: '))
        kali = a*b
        return kali
    def bagi (a,b):
        a=int(input('Masukkan nilai \t: '))
        b=int(input('Masukkan nilai \t: '))
        bagi = a/b
        return bagi


    ulang = 'y'
    while ulang == 'y':
        print('-'*75)
        print('\t\t\t=> KALKULATOR <= ')
        print('1.Pejumlahan \n2.Pengurangan \n3.Perkalian \n4.Pembagian')
        c=input('Masukkan Operasi yang akan anda jalankan : ')
        if c=='1':
            print('-'*75)
            print('\t\t\t= PENJUMLAHAN =')
            print('hasilnya adalah :',jumlah(a,b))
        elif c=='2':
            print('-'*75)
            print('\t\t\t= PENGURANGAN =')
            print('hasilnya adalah :',kurang(a,b))
        elif c=='3':
            print('-'*75)
            print('\t\t\t= PERKALIAN =')
            print('hasilnya adalah :',kali(a,b))
        elif c=='4':
            print('-'*75)
            print('\t\t\t= PEMBAGIAN =')
            print('hasilnya adalah :',bagi(a,b))
        else:
            print('-'*75)
            print('Maaf pilihan yang anda masukkan salah')
        print('-'*75)
        ulang=input('Apakah mau lagi (y/t) : ')
   
        


