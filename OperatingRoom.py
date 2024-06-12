from Character_Creator import Character, Barbarian, characterDict
from WeaponsList import Weapon
from Commands_Index import *

mainChar = Character(name='Kelavir', race='human')
characterDict[mainChar] = None

testDummy = Character(name='Astus', race='human')
characterDict[testDummy] = None

while True:
    initialize()
    mainChar.attack(testDummy)
    testDummy.checkHealth()
    testDummy.attack(mainChar)
    mainChar.checkHealth()

    print()
    print(f'Your HP: {mainChar.health}')
    print(f'Enemy HP: {testDummy.health}')

    #FIXME: process_command(input()) causes immediate crash
    input() # Hit enter to continue the combat