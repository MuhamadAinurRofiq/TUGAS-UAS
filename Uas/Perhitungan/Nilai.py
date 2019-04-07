def nilai():
    from texttable import Texttable
    table = Texttable ()

    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    respon = 'y'

    while respon == 'y':
         print('\n\t\t\t =+= INPUTAN NILAI =+=')
         nama.append (input('\nMasukkan nama \t: '))
         nim.append (input('Masukkan Nim \t: '))
         nilai_tugas.append (input('Nilai tugas \t: '))
         nilai_uts.append (input('Nilai uts \t: '))
         nilai_uas.append (input('Nilai uas \t: '))

         respon = input('\nMau tambah data lagi (y/t) ? ')
         no+=1
         
    for  i in range (no):
         tugas = int(nilai_tugas[i])
         uts = int (nilai_uts[i])
         uas = int (nilai_uas[i])
         akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
         table.set_cols_dtype(['t','t','t','i','i','i','a'])
         table.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1,nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
    print ('\n\t +=+ DETAIL NILAI +=+') 
    print (table.draw())

