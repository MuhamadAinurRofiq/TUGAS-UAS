def pembayaran ():
    from texttable import Texttable
    
    table = Texttable (max_width=700)

    no1 = 0
    pilihan = []
    jawab = 'y'
    nama = []
    nim = []
    kelas = []
    bln=[]
    uts=[]
    uas=[]
    smnr=[]
    kas=[]
    

    while jawab =='y':
        print('='*75)
        print('\t\t\t-----PEMBAYARAN MAHASISWA-----')
        nama.append(input('Masukkan Nama \t: '))
        nim.append(input('Masukkan Nim \t: '))
        kelas.append(input('Masukkan kelas \t: '))
        print('-'*75)
        pilih=input('Apakah anda ingin melakukan pembayaran Bulanan (y/t) \t: ')
        if pilih == 'y':
            a=int(input('Berapa bulan yang akan anda bayar \t\t\t: '))
            b=500000
            bln.append(a*b)
        else:
            bln.append(0)
        print('-'*75)    
        pilih2=input('Apakah anda ingin melakukan pembayaran UTS (y/t) \t: ')
        if pilih2 == 'y':
            a=int(input('Berapa Mapel yang akan anda bayar \t\t\t: '))
            b=50000
            uts.append(a*b)
        else:
            uts.append(0)
        print('-'*75)
        pilih3=input('Apakah anda ingin melakukan pembayaran UAS (y/t) \t: ')
        if pilih3 == 'y':
            a=int(input('Berapa Mapel yang akan anda bayar \t\t\t: '))
            b=50000
            uas.append(a*b)
        else:
            uas.append(0)
        print('-'*75)
        pilih4=input('Apakah anda ingin melakukan pembayaran SEMINAR (y/t) \t: ')
        if pilih4 == 'y':
            b=100000
            smnr.append(b)
        else:
            smnr.append(0)
        print('-'*75)
        pilih5=input('Apakah anda ingin melakukan pembayaran KAS (y/t) \t: ')
        if pilih5 == 'y':
            b=20000
            kas.append(b)
        else:
            kas.append(0)
            
        print('-'*75)
        jawab= input('Apakah anda mau melakukan pembayaran lagi (y/t) \t: ')
        no1+=1
    for i in range (no1):
        bl=int(bln[i])
        ut=int(uts[i])
        ua=int(uas[i])
        sm=int(smnr[i])
        ks=int(kas[i])
        
        total = bl+ut+ua+sm+ks+5000
        table.set_cols_dtype(['t','t','t','t','i','i','i','i','i','i','i'])
        table.add_rows([['NO','NAMA','NIM','KELAS','BULANAN','UTS','UAS','SEMINAR','KAS','ADMIN','TOTAL '],
                        [i+1,nama[i],nim[i],kelas[i],bln[i],uts[i],uas[i],smnr[i],kas[i],5000,total]])
            
    print('-'*75)
    print('\n')
    print('\t\t\t ++-DETAIL PEMBAYARAN-++')
    print(table.draw())        
            
            
            
            
        
        
   
