import os,time
##SETUP MODUL IP
def bersih():
    os.system("clear")
    print(" [=======10")
    os.system("pkg update -y")
    os.system("clear")
    print(" [=================25")
    os.system("pkg upgrade")
    os.system("clear")
    print(" [======================40")
    os.system("pkg install python -y")
    os.system("clear")
    print(" [===========================65")
    os.system("pkg install proot -y")
    os.system("clear")
    print(" [=================================80")
    os.system("pip install requests")
    os.system("clear")
    print(" [========================================90")
    os.system("clear")
    print(" [====================================================100")
def menu():
    bersih()
menu()
import ip
