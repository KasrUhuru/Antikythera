###
### This file.py creates a general framework upon which all creatures in Kythera will be built.

### Humanoids will have more equipment slots than most creatures.

import math, random
from WeaponsList import unarmed

equipmentSlots = {
    'head': 'empty',
    'face': 'empty',
    'neck': 'empty',
    'torso': 'empty',
    'back': 'empty',
    'left hand': 'empty',
    'left finger': 'empty',
    'right hand': 'empty',
    'right finger': 'empty',
    'wrists': 'empty',
    'waist': 'empty',
    'sheathe': 'empty',
    'legs': 'empty',
    'feet': 'empty',
    }

class Character:
    CON = 3
    STR = 3
    POW = 3
    AGI = 3
    WIL = 3
    INT = 3
    stance='neutral'
    def __init__(self,
                name: str,
                race: str,
                health: int,
                stance: str = 'neutral') -> None:
        
        self.name = name
        self.race = race
        self.maxHealth = health
        self.health = health+Character.CON
        self.stance = Character.stance
        self.damageResist = Character.CON//3

        self.hitMod = Character.STR
        self.armor = Character.AGI
        self.weapon = unarmed
        self.damage = self.weapon.damageDice + Character.POW + (Character.STR//3)

        if self.health <= 0:
            print(f'{self.name} has died!')

    def attack(self, target) -> None:
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

# Practice Class Inheritance

# Create the Monk class
class Monk(Character):
    def __init__(self, name: str, race: str, health: int, stance: str) -> None:
        super().__init__(name, race, health, stance)

    def attack(self, target) -> None:
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
            if self.weapon.name == "Unarmed":
                additional_damage = random.randint(1,4)
            damageDealt = max(self.damage + additional_damage - target.damageResist, 0)
            target.health -= damageDealt
            print(f"Calculate {target.name}'s new HP: (base) {self.damage} + (unarmed bonus) {additional_damage} - (resistance) {target.damageResist} = {target.health}")


#Create the Barbarian class
class Barbarian(Character):
    def __init__(self, name: str, race: str, health: int, stance: str) -> None:
        super().__init__(name, race, health, stance)

        self.damageResist = Character.CON//2
        self.damage = self.weapon.damageDice + Character.POW + (Character.STR//2)