#Made By Alyx#4325

import os

print("==================================================================================")
soru = input("[#] Şu An Linux'mu Kullanıyorsun Windows'mu? [L] Linux | [W] Windows [L/W]:")
if soru == "L" or soru == "l":
  os.system("sudo apt-get install pip")
  os.system("sudo pip install requests ")
  os.system("sudo apt-get install python")

elif soru == "W" or soru == "w":
    os.system("pip install requests")

input("Devam Etmek İçin Enter'a Basınız...")