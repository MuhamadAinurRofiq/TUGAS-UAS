def gaji():
    from texttable import Texttable
    table = Texttable ()

    no = 0
    pilihan = []
    respon = 'y'
    nama = []
    jabatan = []
    gaji = []

    while respon == 'y':
        print('\n\t=*= PENGGAJIAN =*=')
        nama.append(input('\nMasukkan nama anda \t: '))
        print ('\n + Pilihan Jabatan + \n- manager \n- spv \n- progamer \n- operator')
        job = input('\nJabatan anda \t\t: ')
        jabatan.append(job)
        if   job == 'manager':
             gaji.append('10.000.000')
        elif job =='spv':
             gaji.append('8.000.000')
        elif job == 'progamer':
             gaji.append('7.000.000')
        elif job == 'operator':
             gaji.append('4.700.000')
        else :
             break
        respon=input('Mau tambah data lagi (y/t) ? ')
        no+=1
        
    for i in range (no):
        table.add_rows([['No','Nama','Jabatan','Gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])
    print('\n ++= DETAIL PENGGAJIAN PT MAJU MUNDUR =++')
    print(table.draw())
    

        
             
            
                    
    
