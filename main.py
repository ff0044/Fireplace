#text based adventure game

#import libraries
from re import T
import time
import sys
from colorama import Fore
import os

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

#cutscene
def cutscene():
    print(Fore.RESET)
    time.sleep(1)
    print(charName + Fore.RESET + " had a sister, a mother, a father and a dog")
    time.sleep(1)
    print(Fore.RESET)
    print("But one day, ")
    time.sleep(2)
    print(Fore.RESET)
    print("A" + Fore.BLUE + " man " + Fore.RESET + "came into the home, looking for some peace")
    time.sleep(2)
    print(Fore.RESET)
    print("The " + Fore.CYAN + "schizophrenia " + Fore.RESET + "had taken over his soul")
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

#skip cutscene question
print("Do you want to skip the cutscene (testing)? [y/n]  >")
skip = input()
if skip == "n":
    cutscene()
elif skip == "y":
    print("You skipped the cutscene")


#Insert Loading animation
def loading():
    print("Loading...")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

loading()

time.sleep(1)
print("\nYou wake up, seeing that all of your family has been gone")
time.sleep(1)
print("")
print("")
print("")
print("")
print("")

#moving variables
north = 'W', 'w'
south = 'S', 's'
east = 'D', 'd'
west = 'A', 'a'

#variables
hallway = Fore.GREEN + 'hallway'
error = Fore.RED + 'Cannot move there'

#start of game
def start():
    print("You are in your bedroom")
    print('All you can hear is white noise, and it is pitch dark')
    print("You can only move north, south, east or west")
    print(Fore.RED + "You can type W, A, S, D to move around" + Fore.RESET)
    time.sleep(1.5)
    print("")
    print("You have the option to exit the door to your left")
    print(f"If you leave, you will be transported to the {hallway}")
    print("")
    print("There is a toy chest behind you, and a bed in front of you")
    print("")
    movement1 = input("What do you do? > ")
    if movement1 == south:
        time.sleep(1)
        print("")
        print("You see a toy chest")
        print("")
        print("You walk towards the toy chest")
        time.sleep(1)
        print("")
        print("You open the toy chest")
        print("")
        print("You see a toy")
        print("")
        print("You pick up the toy")
        print("")
        print("You put the toy in your bag")
        time.sleep(1)
        print("")
    elif movement1 == north or west or east:
        time.sleep(1)
        print(error)



