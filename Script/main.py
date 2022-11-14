#text based adventure game
from variables import *
from imports import *
from cutscene import *
from loading import *
from stairs import *
from hallway import *
from character_bedroom import *

char_info()

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
# run character_bedroom in character_bedroom.py
character_bedroom()