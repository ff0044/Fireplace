#text based adventure game
from imports import *
from cutscene import *
from loading import *
from stairs import *
from hallway import *

#character info
print(Fore.RED + "FIREPLACE")
time.sleep(0.5)
print(Fore.RESET)
print("What is your character's name?")
charName = Fore.GREEN + input()
print("Hello there " + charName + "")
print(Fore.RESET)

#skip cutscene
print("You can skip the cutscene by pressing ENTER")

#cutscene in cutscene.py

#skip cutscene
print("Do you want to skip the cutscene (testing)? [y/n]  >")
skip = input()
if skip == "n":
    cutscene()
elif skip == "y":
    print("You skipped the cutscene")


#Loading animation in loading.py
loading()

time.sleep(1)
print("\nYou wake up, seeing that all of your family has been gone")
time.sleep(1)
print("")
print("")
print("")
print("")
print("")



#variables
hallway = Fore.GREEN + 'hallway' + Fore.RESET
moveerror = Fore.RED + 'Cannot move there'

#character's bedroom


character_bedroom()



#stairs
stairs()