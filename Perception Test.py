#
### Proof of Concept for the perception system in the game:

import random

# Consider moving the ROOMSDAYTIME dictionary to another file.py

# Define all valid commands while this program is small
commandList = {"seek", "end","help", "look", "seek", "search", "remove glasses", "wear glasses", "go"}

# Define valid directions for the player to move
move_choices = {"north", "n", "northeast", "ne", "east", "e", "southeast", "se", "south", "south", "southwest", "sw", "west", "w", "northwest", "north", "into", "up", "down", "in", "out", "through"}

# Define rooms dictionary with keywords
roomsDaytime = {
    "shack interior":{
        "roomDescription": "This cramped home is dim - none of the sunlight seems to penetrate the many holes in the walls and ceiling.\nIt is completely silent, save for your breathing.\nThis room is musty and stale, as if it has been holding its breath for years.",
        "room_DC": 7,
        "roomUnseen": "You sense a rotten stench. It is faint, but persistent. Sometimes it fades away, but it returns.",
        "roomUnseen_DC": 9,
        "roomHidden": "You notice that this stench has been following you as you search this room.",
        "roomHidden_DC": 11,
        "out": "northern shack"
    },
    "northern shack": {
        "roomDescription": "You stand before a run-down, single-story shack. The grass is brown and dead in a 10 meter radius around it. A chill wraps around your body here.\nYou can go INto the shack.\nYou can also go south to the verdant fields.",
        "room_DC": 5,
        "roomUnseen": "Past the cracked windows, in the interior of this shack, the darkness seems to shift as if something is moving around inside. But there is nothing there... you can see the furthest inner wall just fine.",
        "roomUnseen_DC": 7,
        "roomUnheard": "The sounds of splintered glass shifting across dirt can be heard from within. Intermingled with it... raspy, irregular breathing, as if someone were in a panic.",
        "roomUnheard_DC": 8,
        "roomHidden": "",
        "roomHidden_DC": 999,
        "south": "verdant field",
        "s": "verdant field",
        "into shack": "shack interior"
    },
    "verdant field": {
        "roomDescription": "A beautiful, verdant field stretches in all directions. The grass reaches past your boots here.\nTo the north, you can see the outline of a dilapidated cottage.",
        "room_DC": 5,
        "roomUnseen": "A sapphire-encrusted brooch rests by an anthill.",
        "roomUnseen_DC": 7,
        "roomHidden": "A mushroom with legs is crouched in the dense grass!",
        "roomHidden_DC": 10,
        "north": "northern shack",
        "n": "northern shack"
    }
}

# The character has just walked into a room.
# Compare their base Perception skill against the Difficulty of the room.
# It is clear, sunny daytime in a flat, grassy field ; it will not be difficult to see everything.

currentRoom = "verdant field"

# For this room, things are VERY EASY to see.

# Unless the player is very perceptive, they will not notice roomHidden elements immediately.
# In this example, the player is AVERAGE and UNTRAINED.

base=5
wisdomBonus=0
skillBonus=0
itemBonus=0

playerSight = base + wisdomBonus + skillBonus

### The basic LOOK function is a passive use of the Perception skill.
### Since it is passive, it gets no bonus.

def look(playerSight, room_DC):
    print(roomsDaytime[currentRoom]["roomDescription"])
    
    if playerSight >= roomsDaytime[currentRoom]["roomUnseen_DC"]:
        print(roomsDaytime[currentRoom]["roomUnseen"])

    if playerSight >= roomsDaytime[currentRoom]["roomHidden_DC"]:
        print(roomsDaytime[currentRoom]["roomHidden"])

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

### Interpret the basic MOVE function and direction

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

### Prompt the player with the room's Visible contents.

print("************************")
print("Welcome to the world of Kythera!")
print("Its angry gods are currently building this land brick by brick... and you get to see it happen.")

command = input(f"\n************************\n{roomsDaytime[currentRoom]['roomDescription']}\n\nUse HELP to get a list of commands to try!\nYou can also GO [direction] if you see such a path.\n What do you do?\n\n")

while command != "end":
    if command == "look":
        look(playerSight, roomsDaytime[currentRoom]["room_DC"])
    elif command == "search":
        search(playerSight, roomsDaytime[currentRoom]["room_DC"])
    elif command == "seek":
        search(playerSight, roomsDaytime[currentRoom]["room_DC"])
    elif command == "wear glasses":
        itemBonus = 3
        print("You don your glasses...\n Now you can see better!")
    elif command == "remove glasses":
        itemBonus = 0
        print("You remove your glasses.")
    elif command == "help":
        print(f'Here are the following commands you can try:\n\n{commandList}\n')
        print('Bear in mind that this program is still quite fragile and can ONY handle these exact commands so far.')
    process_command(command)
    command = input("\n")
    