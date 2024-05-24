###
### This file.py is an alphabetized collection of all functions within the game.

import math, random

from Environments_List import *
from Character_Creator import *

# This is the command list. User input will be evaluated against this.
commandList = {"seek", "end", "help", "look", "seek", "search", "remove glasses", "wear glasses", "go"}


### We begin with an immediate exception to my rule.
### The PROCESS_COMMAND() function parses the player's input to interact with the environment.
### It is critical to debug this function. It will cascade to all other functions in this index.

# Right now, this function is fragile and easily crashes. 
def process_command(command):
    words = command.split()
    valid = False
    if words[0] == "go":
        valid = True
        if len(words) == 2:
            move(words[1])
        elif len(words) >= 3:
            move((words[1]+ ' ' +words[2]))
    if valid == False:
        print("Sorry, I couldn't understand that. Try trying 'help' for a list of commands to try.")

def hold(item):
    available = True
    global equipment
    if equipment["right hand"]=='empty':
        equipment["right hand"] = item
        print(f'You take the {item} in your right hand.')
    elif equipment["left hand"]=='empty':
        equipment["left hand"] = item
    elif equipment["right hand"] != 'empty' and equipment["left hand"] != 'empty':
        print("Your hands are full!")
        available = False



def get(item):
    global currentRoom
    if item in roomsDaytime[currentRoom]["objects"]:
        hold(item)

### The basic SEARCH function is a deliberate use of the Perception skill.
### It receives a bonus of 1-4 (d4).

def search(playerSight, room):
    print("You peer around the area...")
    foundUnseen = False
    foundHidden = False
    bonus = random.randint(1,4)
    print(roomsDaytime[currentRoom]["roomDescription"])

    # Compare player sight against difficulty checks
    if playerSight + bonus >= roomsDaytime[currentRoom]["roomUnseen_DC"]:
        foundUnseen = True
    if playerSight + bonus >= roomsDaytime[currentRoom]["roomHidden_DC"]:
        foundHidden = True
    
    # Print revealed elements
    if foundUnseen == True:
        print(roomsDaytime[currentRoom]["roomUnseen"])
    if foundHidden == True:
        print(roomsDaytime[currentRoom]["roomHidden"])
    if (foundUnseen == False) and (foundHidden == False):
        print("You don't see anything else.")

### The basic SEEK function allows the player to use their Perception to seek hidden things.
### Add a random bonus between 1-10 (d10) for this attempt.

def seek(playerSight, room):
    print("You peer around the area...")
    foundUnseen = False
    foundHidden = False
    bonus = random.randint(1,10)
    print(roomsDaytime[currentRoom]["roomDescription"])
    
    # The player compares their values against the difficulty checks
    if (playerSight + bonus) >= roomsDaytime[currentRoom]["roomUnseen_DC"]:
        foundUnseen = True
    if (playerSight + bonus) >= roomsDaytime[currentRoom]["roomHidden_DC"]:
        foundHidden = True
    
    # If the player fails both checks
    if foundUnseen == True:
        print(roomsDaytime[currentRoom]["roomUnseen"])
    if foundHidden == True:
        print(roomsDaytime[currentRoom]["roomHidden"])
    if (foundUnseen == False) and (foundHidden == False):
        print("You don't see anything else.")

### The basic LOOK function is a passive use of the Perception skill.
### Since it is passive, it gets no bonus.

def look(playerSight, room_DC):
    print(roomsDaytime[currentRoom]["roomDescription"])
    
    if playerSight >= roomsDaytime[currentRoom]["roomUnseen_DC"]:
        print(roomsDaytime[currentRoom]["roomUnseen"])

    if playerSight >= roomsDaytime[currentRoom]["roomHidden_DC"]:
        print(roomsDaytime[currentRoom]["roomHidden"])

### Enable the player to move to other rooms
def move(direction):
    global currentRoom
    if direction in roomsDaytime[currentRoom]:
        currentRoom = roomsDaytime[currentRoom][direction]
        print("************************")
        print(f"Moved to {currentRoom}.")
        print(roomsDaytime[currentRoom]["roomDescription"])
    else:
        print("You can't go that way.")



