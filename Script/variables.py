from imports import *


# character info
def char_info():
    print(Fore.RED + "FIREPLACE")
    time.sleep(0.5)
    print(Fore.RESET)
    print("What is your character's name?")
    charname1 = Fore.GREEN + input()
    print("Hello there " + charname1 + ".")
    print(Fore.RESET)

#variables
hallway = Fore.GREEN + 'hallway' + Fore.RESET
moveerror = Fore.RED + 'Cannot move there'
charname = charname1