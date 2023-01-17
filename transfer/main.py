#imports
from re import T 
import time 
import sys 
from colorama import *
import os
from player import *

#variables
hallway = Fore.GREEN + 'hallway' + Fore.RESET
moveerror = Fore.RED + 'Cannot move there'

#character info
print(Fore.RED + "FIREPLACE")
time.sleep(0.5)
print(Fore.RESET)
player = Player(input("What is your name > "))

print("Hello there " + player.name + ".")
print(Fore.RESET)

#cutscene
print("You can skip the cutscene by pressing ENTER")
def cutscene():
    print(Fore.RESET)
    time.sleep(1)
    print(player.name + Fore.RESET + " have a sister, a mother, a father and a dog")
    time.sleep(1)
    print(Fore.RESET)
    print("But one day, ")
    time.sleep(2)
    print(Fore.RESET)
    print("A" + Fore.BLUE + " man " + Fore.RESET + "came into the home, looking for some peace")
    time.sleep(2)
    print(Fore.RESET)
    print("The " + Fore.CYAN + "devil " + Fore.RESET + "had taken over his soul")
    time.sleep(1)
    print(Fore.RESET)
    print("The" + Fore.BLUE + " man " + Fore.RESET + "made a deal with the voices in his head")
    time.sleep(2)
    print(Fore.RESET)
    print(Fore.CYAN + "'You want some peace, kill a family'")
    time.sleep(2)
    print(Fore.RESET)
    print("The" + Fore.BLUE + " man " + Fore.RESET + "replied with: ")
    time.sleep(2)
    print(Fore.RESET)
    print(Fore.BLUE + "'Why should I kill an innocent family just for your sake?'")
    time.sleep(2)
    print(Fore.RESET)
    print(Fore.CYAN + "'Do you want the voices out of your head or not?'")
    time.sleep(2)
    print(Fore.RESET)
    print(Fore.RED + "SLASH")
    time.sleep(2)
    print(Fore.RESET)
    print("HELPPPP")