from Environments_List import roomsDaytime
from Commands_Index import commandList,process_command,hold,get,search,seek,look
from Character_Creator import equipment

def main():
    currentRoom = "verdant field"
    roomsDaytime[currentRoom]["objects"].append("brooch")
    roomsDaytime[currentRoom]["objects"].append("bone")
    roomsDaytime[currentRoom]["objects"].append("whip")

    base=5
    wisdomBonus=0
    skillBonus=0
    itemBonus=0
    playerSight = base + wisdomBonus + skillBonus

    command = input("Welcome to the world of Kythera!")

    while command != 'quit':
        process_command(command)

if __name__ == '__main__':
    main()