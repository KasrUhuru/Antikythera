from Environments_List import *
from Commands_Index import *
from Character_Creator import *

currentRoom = "verdant field"

roomsDaytime[currentRoom]["objects"].append("brooch")
roomsDaytime[currentRoom]["objects"].append("bone")
roomsDaytime[currentRoom]["objects"].append("whip")

def hold(item):
    available = True
    global equipment
    if equipment["right hand"]=='empty':
        equipment["right hand"] = item
        print(f'You take the {item} in your right hand.')
    elif equipment["left hand"]=='empty':
        equipment["left hand"] = item
        print(f'You take the {item} in your left hand.')
    elif equipment["right hand"] != 'empty' and equipment["left hand"] != 'empty':
        print("Your hands are full!")
        available = False

def get(item):
    global currentRoom
    if item in roomsDaytime[currentRoom]["objects"]:
        hold(item)
    else:
        print("You don't see that here.")

print('On the ground you see', end=' ')
for index, object in enumerate(roomsDaytime[currentRoom]["objects"]):
    if index < len(roomsDaytime[currentRoom]["objects"]) - 1:
        print(f'a {object},', end=' ')
    else:
        print(f'and a {object}.')

