import variables
from imports import *
from hallway import *
from variables import *
def character_bedroom():
    print("You are in your bedroom")
    print('All you can hear is white noise, and it is pitch dark')
    print("You can only move north, south, east or west")
    print(Fore.RED + "You can type 1 (W), 2 (A), 3 (S), 4 (D) to move around" + Fore.RESET)
    time.sleep(1.5)
    print("")

    print("You have the option to exit the door to your left")
    print(f"If you leave, you will be transported to the {variables.hallway}")
    print("")
    print("There is a toy chest behind you, and a bed in front of you")
    print("")

    movement1 = input("What do you do? >>")

    if movement1 == '3':
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
        print("Acquired toy")
        time.sleep(1)
        character_bedroom()
    if movement1 == '1':
        time.sleep(1)
        print("")
        print("You walk towards the bed")
        print("")
        print("You want to sleep, but you are too curious to")
        print("")
        character_bedroom()
    if movement1 == '2':
        hallway()
    if movement1 == '4':
        print(moveerror)