from Perhitungan.Gaji import gaji
from Perhitungan.Nilai import nilai
from Perhitungan.Pembayaran import pembayaran
from Perhitungan.Kalkulator import kalkulator
import getpass

def login():
    print('=+= Login =+=')
    user=input('Username : ')
    password=getpass.getpass('Password : ')
    if user == 'aino' and password == 'gratisan':
        mulai()
    else:
        print('Maaf username / password yang anda masukkan salah, Mohon ulangi')
        login()

def mulai ():
    print('\n\t\t\t +=+= PILIHAN PROGAM =+=+ \n\n1.PENGGAJIAN \n2.INPUT NILAI \n3.PEMBAYARAN \n4.KALKULATOR')
    pilih = input('\nMasukkan pilihan anda : ')
    if   pilih == '1':
         print('-'*75)
         gaji()
    elif pilih == '2':
         print('-'*75)
         nilai()
    elif pilih == '3':
         print('-'*75)
         pembayaran()
    elif pilih == '4':
         print('-'*75)
         kalkulator()         
    else :
         print('\nMaaf pilihan yang anda masukkan salah, silahkan ulangi pilihan anda.')
    jawab ()
    
def jawab ():
    tanya = input('\nApakah anda ingin menjalan kan progam lagi (y/t): ')
    if   tanya == 'y':
         mulai()
    else :
         print('='*75)
         print('\n\t\t\t+++ TERIMAKASIH +++')
login()        

