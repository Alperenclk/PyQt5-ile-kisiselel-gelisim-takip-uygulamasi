import sqlite3
from os import close
from sqlite3.dbapi2 import Cursor
import sys
import time
from datetime import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ilkVersiyonUI import *

# region  ******uygulama oluşturma******
uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


# endregion

# region   *********VERİ TABANI*********
global cursor
global conn

conn = sqlite3.connect('ilkVersiyonDB.db')
cursor = conn.cursor()

sorguCreTblAna = ("CREATE TABLE IF NOT EXISTS GIRIS(id INTEGER PRIMARY KEY AUTOINCREMENT,kullanici_adi TEXT,ktpGunHedf  text,ktpGunIht  text,ingGunHedf  text,ingGunIht  text,FDBGunHedf  text,FDBGunIht  text,kayitT text)")
sorguCreTblktp = ("CREATE TABLE IF NOT EXISTS KITAP(id INTEGER PRIMARY KEY AUTOINCREMENT,kullanici_adi TEXT,ktpGunZmn  text,gunPuan text,topPuan text,kayitT text)")
sorguCreTbling = ("CREATE TABLE IF NOT EXISTS INGILIZCE(id INTEGER PRIMARY KEY AUTOINCREMENT,kullanici_adi TEXT,ingGunZmn  text,gunPuan text,topPuan text,kayitT text)")
sorguCreTblFDB = ("CREATE TABLE IF NOT EXISTS FDB(id INTEGER PRIMARY KEY AUTOINCREMENT,kullanici_adi TEXT,FDBGunZmn  text,gunPuan text,topPuan text,kayitT text)")
cursor.execute(sorguCreTblAna)
cursor.execute(sorguCreTblktp)
cursor.execute(sorguCreTbling)
cursor.execute(sorguCreTblFDB)
conn.commit()


# endregion

# region *******EKLE*****
def EKLE():
    _time = time.strftime("%x %X")
    _lneKayKulAdi = ui.lneKullanici.text()
    _lnektpGunHdf = ui.lneKtpGunHdf.text()
    _lneKtpGunIhtZmn = ui.lneKtpGunIhtZmn.text()
    _lneKtpGunZmn = ui._lneKtpGunZmn.text()
    _lneIngGunHdf = ui._lneIngGunHdf.text()
    _lneIngGunIhtZmn = ui.lneIngGunIhtZmn.text()
    _lneIngGunZmn = ui.lneIngGunZmn.text()
    _lneFDBGunHdf = ui.lneFDBGunHdf.text()
    _lneFDBGunIhtZmn = ui.lnefdbGunIhtZmn.text()
    _lneFDBGunZmn = ui.lneFDBGunZmn.text()




    while True:
        try:  
            cursor.execute(f"SELECT kullanici_adi from GIRIS WHERE kullanici_adi ='{_lneKayKulAdi}'")
            if not cursor.fetchone() == None:

                _gunPuan =0
                gunlukTop =0
                _gunPuan= (int(_lneKtpGunZmn) / int(_lneKtpGunIhtZmn)) * 10
                _gunPuan =_gunPuan.__round__(2)
                gunlukTop += _gunPuan
                _gunPuan =str(_gunPuan)
                
                cursor.execute("INSERT INTO KITAP(kullanici_adi,ktpGunZmn,gunPuan,kayitT)VALUES(?,?,?,?)",
                    (_lneKayKulAdi,_lneKtpGunZmn,_gunPuan,_time ))
                    
                
                _gunPuan =0
                _gunPuan= (int(_lneIngGunZmn) / int(_lneIngGunIhtZmn)) * 10
                _gunPuan =_gunPuan.__round__(2)
                gunlukTop += _gunPuan
                _gunPuan =str(_gunPuan)
                

                cursor.execute("INSERT INTO INGILIZCE(kullanici_adi,ingGunZmn,gunPuan,kayitT)VALUES(?,?,?,?)",
                    (_lneKayKulAdi,_lneIngGunZmn,_gunPuan,_time ))
    
                _gunPuan =0
                _gunPuan= (int(_lneFDBGunZmn) / int(_lneFDBGunIhtZmn)) * 10
                _gunPuan =_gunPuan.__round__(2)
                gunlukTop += _gunPuan
                _gunPuan =str(_gunPuan)

                cursor.execute("INSERT INTO FDB(kullanici_adi,FDBGunZmn,gunPuan,kayitT)VALUES(?,?,?,?)",
                    (_lneKayKulAdi,_lneFDBGunZmn,_gunPuan,_time ))

                ui.lbBosGun.setText(str(gunlukTop))

                break
            else:
                cursor.execute("INSERT INTO GIRIS(kullanici_adi,ktpGunHedf,ktpGunIht,ingGunHedf,ingGunIht,FDBGunHedf,FDBGunIht,kayitT)VALUES(?,?,?,?,?,?,?,?)",
                    (_lneKayKulAdi,_lnektpGunHdf,_lneKtpGunIhtZmn,_lneIngGunHdf,_lneIngGunIhtZmn,_lneFDBGunHdf,_lneFDBGunIhtZmn,_time ))
                continue
                
    
        except Exception as hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(hata))
            break

                   
    conn.commit()

# endregion 

# region *******CIKIS*****

def CIKIS():
    cevap = QMessageBox.question(
        penAna, 'Exit', 'Ciksi yapmak istediginize emin misiniz?', QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        conn.close()
        sys.exit(uygulama.exec_())
    else:
        penAna.show()

# endregion

# region *******BILGILER*****

def BILGILER():
    _lneKayKulAdi = ui.lneKullanici.text()
    _lnektpGunHdf = ui.lneKtpGunHdf.text()
    _lneKtpGunIhtZmn = ui.lneKtpGunIhtZmn.text()
    _lneIngGunHdf = ui._lneIngGunHdf.text()
    _lneIngGunIhtZmn = ui.lneIngGunIhtZmn.text()
    _lneFDBGunHdf = ui.lneFDBGunHdf.text()
    _lneFDBGunIhtZmn = ui.lnefdbGunIhtZmn.text()
    _time = time.ctime()



    try:
        
        cursor.execute(f"SELECT kullanici_adi from GIRIS WHERE kullanici_adi ='{_lneKayKulAdi}'")
        if not cursor.fetchone() == None:
            cursor.execute(f"SELECT ktpGunHedf,ktpGunIht,ingGunHedf,ingGunIht,FDBGunHedf,FDBGunIht from GIRIS WHERE kullanici_adi ='{_lneKayKulAdi}'")
            secili = cursor.fetchone()
            ui.lneKtpGunHdf.setText(secili[0])
            ui.lneKtpGunIhtZmn.setText(secili[1])
            ui._lneIngGunHdf.setText(secili[2])
            ui.lneIngGunIhtZmn.setText(secili[3])
            ui.lneFDBGunHdf.setText(secili[4])
            ui.lnefdbGunIhtZmn.setText(secili[5])
        

        else:
            cevap = QMessageBox.critical(penAna,'BULUNAMADI','BOYLE BIR KULLANICI BULUNAMADI')

               
  
    except Exception as hata:
        ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(hata))

    conn.commit()

    
  # endregion  

# region *******KALAN*****
def KALAN():

    simdiTarih = time.strftime('%x')            
    _lneKayKulAdi = ui.lneKullanici.text()

    # KITAP

    cursor.execute(f"SELECT kayitT from KITAP WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    
    tarih =cursor.fetchone()
    ilkTarih =tarih[0][:8]
    d1 = datetime.strptime(ilkTarih,"%m/%d/%y")
    d2 = datetime.strptime(simdiTarih,"%m/%d/%y")

    cursor.execute(f"SELECT ktpGunHedf from GIRIS WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    gunSayi =cursor.fetchone()

    kalanGun = int(gunSayi[0])+abs((d2 - d1).days)
    ui.lbBos1.setText(str(kalanGun))

    #INGILIZCE

    cursor.execute(f"SELECT kayitT from INGILIZCE WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    
    tarih =cursor.fetchone()
    ilkTarih =tarih[0][:8]
    d1 = datetime.strptime(ilkTarih,"%m/%d/%y")
    d2 = datetime.strptime(simdiTarih,"%m/%d/%y")

    cursor.execute(f"SELECT ingGunHedf from GIRIS WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    gunSayi =cursor.fetchone()

    kalanGun = int(gunSayi[0])+abs((d2 - d1).days)
    ui.lbBos2.setText(str(kalanGun))

    #FDB

    cursor.execute(f"SELECT kayitT from FDB WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    
    tarih =cursor.fetchone()
    ilkTarih =tarih[0][:8]
    d1 = datetime.strptime(ilkTarih,"%m/%d/%y")
    d2 = datetime.strptime(simdiTarih,"%m/%d/%y")

    cursor.execute(f"SELECT FDBGunHedf from GIRIS WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    gunSayi =cursor.fetchone()

    kalanGun = int(gunSayi[0])+abs((d2 - d1).days)
    ui.lbBos3.setText(str(kalanGun))

# endregion

# region *******PUAN*****
def PUAN():
    _lneKayKulAdi = ui.lneKullanici.text()
    cursor.execute(f"SELECT gunPuan from KITAP WHERE kullanici_adi = '{_lneKayKulAdi}' ")
    



# endregion


# region *******SINYAL/SLOT*****

ui.btngiris.clicked.connect(EKLE)
ui.btngiris.clicked.connect(KALAN)
ui.btnBilgiler.clicked.connect(BILGILER)
ui.btnCikis.clicked.connect(CIKIS)
# endregion

sys.exit(uygulama.exec_()) 