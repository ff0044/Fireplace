from imports import *
from loading import *

def hallway():
    #loading
    print("Loading...")
    loading()

    print("You are in the hallway")
    print(f"There is your {Fore.RED}bedroom{Fore.RESET} to the right of you")
    print("Your parents room and bathroom is to the left of you")
    print("Your sister has her room behind you")
    print("In front of you, you can go down the stairs to the bottom floor")
    movement2 = input("What do you pick? >")
    #movement 2
    if movement2 == '1':
        stairs()
    elif movement2 == '2':
        print("not ready yet")
    elif movement2 == '3':
        print("not ready yet")
    elif movement2 == '4':
        print("not ready yet")