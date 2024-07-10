from Character_Creator import Character, Barbarian, characterDict
from WeaponsList import Weapon
from Commands_Index import *

mainChar = Character(name='Mistlethur', race='human')
characterDict[mainChar] = None

testDummy = Character(name='Uhuru', race='human')
characterDict[testDummy] = None

while True:
    initialize()
    mainChar.attack(testDummy)
    testDummy.checkHealth()
    testDummy.attack(mainChar)
    mainChar.checkHealth()

    print()
    print(f"{mainChar.name}'s HP: {mainChar.health}")
    print(f"{testDummy.name}'s HP: {testDummy.health}")

    #FIXME: process_command(input()) causes immediate crash
    input() # Hit enter to continue the combat
