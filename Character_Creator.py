###
### This file.py creates a general framework upon which all creatures in Kythera will be built.

### Humanoids will have more equipment slots than most creatures.

import math, random
from WeaponsList import unarmed

# Goals for implementation:
# 1. Character needs to be unarmored, unarmed, and neutral. DONE!!
# 2. Class functions need to update character armor, equipment, and stance in a way that can interact with their environment.
# 3. Equipment objects should read their values into the Character to update statistics.
# 4. Changing stances should first undo their modifications to Character statistics, then implement the new stance modifications. DONE!!
# 5. Initialize an inventory.
# 6. Define functions to: GET items from the environment; GET items from the inventory; EQUIP items; HOLD items in one or both hands; STORE items.
# 7. Initialize a character creator menu to allow the player to choose their race, name, and class.
characterDict = {}

class Character:
    CON = 3
    STR = 3
    POW = 3
    AGI = 3
    WIL = 3
    INT = 3
    def __init__(self,
                name: str,
                race: str,) -> None:
        
        self.name = name
        self.race = race
        self.health = 10 + Character.CON
        self.maxHealth = self.health
        self.stamina = Character.CON * 5
        self.mana = Character.WIL/3 + (Character.INT*3)
        self.experience = 0
        self.skillPoints = Character.INT
        self.alive = True
        self.stance = 'neutral'
        self.damageResist = Character.CON//3

        self.hitMod = Character.STR
        self.armor = Character.AGI
        self.weapon = None
        self.damage = (self.weapon.damageDice if self.weapon else 0) + Character.POW + (Character.STR//3)

    def checkHealth(self):
        if self.health <= 0:
            self.alive = False
            print(f'{self.name} has died!')
            self.die()

    def die(self):
        if self.name in characterDict:
            del characterDict[self.name]

    def attack(self, target) -> None:
        if self.alive:
            hit = False
            additional_damage = 0

            print(f"{self.name} attacks {target.name}...")

            # Calculate attack
            attackBase = self.hitMod
            attackBonus = random.randint(1,20)
            attackRoll = attackBase + attackBonus

            # Calculate opposing defense roll
            defenseBase = target.armor
            defenseBonus = random.randint(1,20)
            defenseRoll = defenseBase + defenseBonus

            #Evaluate the hit
            if attackRoll >= defenseRoll:
                hit = True
                print(f'Attack Roll HITS (base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
                print(f'and hits!\n')
            elif attackRoll < defenseRoll:
                print(f'Attack Roll FAILS (base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
                print(f'and misses!\n')

            if hit is True:
                damageDealt = max(self.damage + additional_damage - target.damageResist, 0)
                target.health -= damageDealt
                print(f"Calculate {target.name}'s new HP: (base) {self.damage} + (unarmed bonus) {additional_damage} - (resistance) {target.damageResist} = {target.health}")
        else:
            print(f'{self.name} is dead and cannot attack.')
    def checkStance(self):
        stanceList = {'neutral': {'damageResist':0, 'damage': 0, 'hitMod': 0, 'armor':0},
                      'aggressive': {'damageResist':0, 'damage': 2, 'hitMod': 2, 'armor': -2},
                      'defensive': {'damageResist': 2, 'damage': -2, 'hitMod': -2, 'armor': 2}}
        print(f'Your stance is currently {self.stance}.')
        for stanceKey, stanceValue in stanceList[self.stance].items():
            print(f'{stanceKey}: {stanceValue}')

    def changeStance(self, newStance):
        #List the possible stances
        stanceList = {'neutral': {'damageResist':0, 'damage': 0, 'hitMod': 0, 'armor':0},
                      'aggressive': {'damageResist':0, 'damage': 2, 'hitMod': 2, 'armor': -2},
                      'defensive': {'damageResist': 2, 'damage': -2, 'hitMod': -2, 'armor': 2}}
        
        # Check the validity of the stance
        if newStance in stanceList:
            # Undo the statistic modifications of the current stance!
            self.damageResist -=stanceList[self.stance]['damageResist']
            self.damage -=stanceList[self.stance]['damage']
            self.hitMod -=stanceList[self.stance]['hitMod']
            self.armor -=stanceList[self.stance]['armor']
            # Apply the statistic modifications of the new stance!
            self.stance = newStance
            self.damageResist += stanceList[newStance]['damageResist']
            self.damage -=stanceList[newStance]['damage']
            self.hitMod -=stanceList[newStance]['hitMod']
            self.armor -=stanceList[newStance]['armor']
        
        # Handle error and present alternatives
        elif newStance not in stanceList:
            print(f'That is not a valid stance. Valid stances are:')
            for stanceKey in stanceList.keys():
                print(stanceKey)

### Practice Class Inheritance

# Create the Monk class
## FIXME: Define a better way of calculating unarmed damage.


#Create the Barbarian class
class Barbarian(Character):
    def __init__(self, name: str, race: str, health: int, stance: str) -> None:
        super().__init__(name, race, health, stance)

        self.damageResist = Character.CON//2
        self.damage = self.weapon.damageDice + Character.POW + (Character.STR//2)