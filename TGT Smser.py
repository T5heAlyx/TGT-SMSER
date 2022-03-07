#Made By Alyx#2795

import requests
import time
from os import system as s
import os

#Giriş Credits Bölümü:
while (True):
 tgtsmser = """
  _______ _____ _______    _____ __  __  _____ ______ _____  
 |__   __/ ____|__   __|  / ____|  \/  |/ ____|  ____|  __ \ 
    | | | |  __   | |    | (___ | \  / | (___ | |__  | |__) |
    | | | | |_ |  | |     \___ \| |\/| |\___ \|  __| |  _  /                            
    | | | |__| |  | |     ____) | |  | |____) | |____| | \ \ 
    |_|  \_____|  |_|    |_____/|_|  |_|_____/|______|_|  \_\                                 
"""
# Made By Alyx#2795

 credits = """
                              |_____________________|
                              |> Made By Alyx#2795 <|        	             
_______________________________|> Turkish Guy Tim <|__________________________________
|> İstediginiz Telefon Numarasına Her Gün Sadece 1 Defa Mesaj Atma Hakkınız Vardır!  <|
|> Mesajınızdaki karakter sayısı 70'i geçmemelidir.                                  <|
|> Eğer Mesajınızı Gönderdikten Sonra False Görürseniz Telefon Numaranız Geçersizdir.<|
|> Youtube: https://www.youtube.com/channel/UCXspb19nmlqMkuakJklcqsw                 <|                    
|> Discord: https://discord.gg/eZKQWcmuNy (:)     (:)(:)   (:)(:)   (:)(:)   (:)(:)  <|
|> Web Site: http://turkishguyteam.rf.gd/   (:)   (:)(:)   (:)(:)   (:)(:)   (:)(:)  <|
|_____________________________________________________________________________________|
"""
 print(tgtsmser)
 print(credits)

#Kodlar:

 input("[#] Programı Başlatmak İçin Enter'a Basınız...")

 print("=================================")
 tel = input("[#] Bir Telefon Numarası Giriniz: ")
 print("=======================")
 mesaj = input("[#] Mesajınızı Giriniz: ")

 time.sleep(0.3)
 kisalt = mesaj[0:70]

 print("\n[%] Mesajınızın Gönderilebilecek Kısmı Aşagıdaki Gibidir.\n","\n" + kisalt)  #Made By Alyx#2795

 gonder = input("\n[#] Mesajınız Gönderilsinmi? [Y/n]: ")

 if gonder == "y" or gonder == "Y":
    print("\n","[%] Mesajınız Gönderiliyor...\n","=======================","\n Telefon: " + tel + "\n","Mesaj: " + kisalt + "\n")  #Made By Alyx#4325
    time.sleep(2)
    res = requests.post('https://textbelt.com/text',{
        'phone': tel,
        'message': kisalt,
        'key': 'textbelt',})
    print(res.json())
    input("[#] Devam Etmek İçin Enter'a Basınız...")

    if soru == "L" or soru == "l":
        os.system("clear")

    elif soru == "W" or soru == "w":
        os.system("cls")
    else:
       pass


 # Made By Alyx#2795

 elif gonder == "n" or gonder == "N":
  em = input("[%] Programdan Çıkmak İçin [Y/y] \n[%] Ana Menüye Dönmek İçin [N/n] \n[#]:")  #Made By Alyx#2795

  if em == "Y" or em == "y":
       print("\n[%] Çıkılıyor...")
       time.sleep(1)
       if soru == "W" or soru == "w":
        os.system("cls")

       elif soru == "L" or soru == "l":
         os.system("clear")
       else:
         pass

       break



  elif em == "N" or em == "n":
        pass



 else:
    print("\n[#] Bir Hata Oluştu!")

#Made By Alyx#2795
