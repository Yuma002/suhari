import requests
import json
import os


def cler():
   os.system("clear")
def menu2():
    cler()
menu2()

def cler1():
    print("")
def menu3():
    cler1()
menu3()

def cler4():
    print("  =================== P̴ R̴ O̴ J̴ E̴ C̴ K̴  ̴ Y̴ U̴ M̴ A̴ ========================")
def menu4():
    cler4()
menu4()

ipaddress = input("  ɪᴘ ᴀᴅᴅʀᴇꜱꜱ : ")
def sel():
    print("  =====================================================================")
def menu5():
    sel()
menu5()
iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")

if iprequest.status_code == 200:
	ipdata = json.loads(iprequest.text)

	if ipdata["status"] == "success":
		for key in ipdata:
			print(f"{key.capitalize()} : {ipdata[key]}")
			
			if key == "lon":
				lat = ipdata["lat"]
				lon = ipdata["lon"]
				maps = f"https://www.google.com/maps/@{lat},{lon},9z"
				print(f"Maps : {maps}")


def ulang():
    print("  =================== 𝐈𝐍𝐅𝐎 𝐋𝐎𝐊𝐀𝐒𝐈 𝐀𝐃𝐀 𝐃𝐈 𝐀𝐓𝐀𝐒 𝐘𝐀 𝐆𝐀𝐍 ====================")
def menus():
   ulang()
menus()
