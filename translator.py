from defs import *

import time

try:
    from colorama import Fore, Back, Style
except:
    print("You need to install colorama\nUse 'pip install colorama'")

TEXT = """
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝╚█████╗░
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗░╚═══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

████████╗██████╗░░█████╗░███╗░░██╗░██████╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"""

print(Fore.LIGHTYELLOW_EX + TEXT)
print(Fore.CYAN + "by Dev_Cored\n\n" + Style.RESET_ALL)
INPUT_SIGN = Fore.YELLOW + Style.BRIGHT + ">" + Style.RESET_ALL
while True:
    print(Fore.MAGENTA + "Chose the action: \n0 - Exit\n1 - Encrypt\n2 - Decrypt\nAdd f for your choice to save results in file. Example: 1f or 2f\n\n")


    cmd = input(INPUT_SIGN)
    if cmd == "0":
        break
    elif cmd == "1":
        encrypt(False)
    elif cmd == "1f":
        encrypt(True)
    elif cmd == "2":
        decrypt(False)
    elif cmd == "2f":
        decrypt(True)




print(Fore.RED+Style.BRIGHT+"Programm has been closed. Thanks for using!")
input("Press enter 4 times to exit.")
input("...")
input("..")
input("." + Style.RESET_ALL)