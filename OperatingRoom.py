from Character_Creator import Character, Monk, Barbarian
from WeaponsList import Weapon, unarmed

mainChar = Monk(name='Kaelaviv', race='human', health=50, stance='neutral')

testDummy = Character(name='Astus', race='human', health=50, stance='neutral')

while True:

    mainChar.attack(testDummy)
    testDummy.attack(mainChar)

    print()
    print(f'Your HP: {mainChar.health}')
    print(f'Enemy HP: {testDummy.health}')

    input()