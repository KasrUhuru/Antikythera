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
    def __init__(self,
                name: str,
                race: str,) -> None:
        
        self.CON = 3
        self.STR = 3
        self.POW = 3
        self.AGI = 3
        self.WIL = 3
        self.INT = 3
        self.PER = 3
        self.alive = True

        self.name = name
        self.race = race
        self.health = 10 + self.CON
        self.maxHealth = self.health
        self.damageResist = self.CON//3
        self.stamina = self.CON * 5
        self.mana = self.WIL/3 + (self.INT*3)
        self.limbs = {
            'head': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'torso': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'left leg': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'right leg': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'left arm': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'right arm': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'left hand': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist},
            'right hand': {'maxHealth': self.CON, 'health': self.CON, 'injured': False, 'damageResist': self.damageResist}
            }
        
        self.experience = 0
        self.skillPoints = self.INT
        self.perception = self.PER
        
        self.armor = self.AGI
        self.hitMod = self.STR
        self.aiming = False
        self.targetLimb = 'torso'
        self.weapon = unarmed
        #self.damage = self.POW + (self.weapon.damageStat//2) + self.weapon.damageDice
        self.damage = self.POW + self.weapon.damageDice
        self.stance = 'neutral'

        self.inventory = None
        self.equipment = {
            'head':'empty',
            'leftGlove':'empty',
            'leftHand':'empty',
            'rightGlove':'empty',
            'rightHand':'empty',
            'chest':'empty',
            'back':'empty',
            'pack':'empty',
            'ring':'empty'
            }


    def checkHealth(self) -> None:
        if self.health <= 0:
            self.alive = False
            print(f'{self.name} has died!')
            self.die()

    def die(self) -> None:
        if self.name in characterDict:
            del characterDict[self.name]

    def get(self, object) -> None:
        if self.equipment['leftHand'] == 'empty':
            self.equipment['leftHand'] = object
            print(f'You take the {object.name} in your left hand.')
        elif self.equipment['rightHand'] == 'empty':
            self.equipment['rightHand'] = object
            print(f'You take the {object.name} in your right hand.')

    def equip(self, object) -> None:
        if not object.equipable:
            print('This cannot be worn. EXAMINE the {object.name} more closely.')
        
    # Target a specific part of the enemy, such as their sword arm or their head
    def setAim(self, target, limb):
        self.aiming = True
        self.targetLimb = target.limbs[limb]

    # Attacks return to default: target a random part of the enemy
    def stopAim(self):
        self.aiming = False
    
    # Determine if the target has natural resistance to incoming damage type
    def checkResist(self, target):
        generalResist = target.damageResist
        #FIXME: Implement specificResist

    def attack(self, target) -> None:
        if self.alive:
            hit = False
            critHit = False
            additional_damage = 0

            print(f"{self.name} attacks {target.name}...")

            # Determine target
            if self.aiming is False:
                randomTarget = random.randint(1,9)
                if randomTarget == 1:
                    self.targetLimb = 'head'
                elif randomTarget == 2:
                    self.targetLimb ='torso'
                elif randomTarget == 3:
                    self.targetLimb = 'left leg'
                elif randomTarget == 4:
                    self.targetLimb = 'right leg'
                elif randomTarget == 5:
                    self.targetLimb = 'right arm'
                elif randomTarget == 6:
                    self.targetLimb = 'left arm'
                elif randomTarget == 7:
                    self.targetLimb = 'right hand'
                elif randomTarget == 8:
                    self.targetLimb = 'left hand'

            # Calculate attack
            attackBase = self.hitMod
            attackBonus = random.randint(1,20)
            attackRoll = attackBase + attackBonus

            # Calculate opposing defense roll
            defenseBase = target.armor
            defenseBonus = 10
            defenseRoll = defenseBase + defenseBonus

            # Evaluate the hit
            if attackRoll >= defenseRoll + 10:
                critHit = True
                print(f'CRITICAL HIT!')
                print(f'(base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
                print(f'{self.name} strikes {target.name} in the {self.targetLimb}!\n')
            elif attackRoll >= defenseRoll:
                hit = True
                print(f'Attack Roll HITS (base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
                print(f'...and hits!')
                print(f'{self.name} strikes {target.name} in the {self.targetLimb}!\n')
            elif attackRoll < defenseRoll - 10:
                print(f'CRITICAL MISS!')
                print(f'(base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
            elif attackRoll < defenseRoll:
                print(f'Attack Roll FAILS (base) {attackBase} + (bonus) {attackBonus} = {attackRoll} versus {defenseRoll} (base) {defenseBase} + (bonus) {defenseBonus}')
                print(f'...and misses!\n\n')
            if critHit is True:
                # Critical hits ignore damage resistances and add a dice roll worth of damage
                additional_damage = self.damage
                damageDealt = max(self.damage + additional_damage, 0)
                ## Implement a function dealDamage() that assesses resistances and vulnerabilities relative to the attacker's damage types
                ## Replace the line of code below with this function
                target.health -= damageDealt
                print(f"{target.name}'s new HP: (base damage) {self.damage} + (bonus damage) {additional_damage} - (resistance) {target.damageResist} = {target.health}\n")

            if hit is True:
                damageDealt = max(self.damage + additional_damage - max(target.damageResist, target.limbs[self.targetLimb]['damageResist']), 0)
                ## Implement a function dealDamage() that assesses resistances and vulnerabilities relative to the attacker's damage types
                ## Replace the line of code below with this function
                target.health -= damageDealt
                #FIXME:target.health -= checkResistances(damageDealt)
                print(f"{target.name}'s new HP: (base damage) {self.damage} + (bonus damage) {additional_damage} - (resistance) {target.damageResist} = {target.health}\n")
        else:
            print(f'{self.name} is dead and cannot attack.')
            
    def checkStance(self) -> None:
        stanceList = {'neutral': {'damageResist':0, 'damage': 0, 'hitMod': 0, 'armor':0},
                      'aggressive': {'damageResist':0, 'damage': 2, 'hitMod': 2, 'armor': -2},
                      'defensive': {'damageResist': 2, 'damage': -2, 'hitMod': -2, 'armor': 2}}
        print(f'Your stance is currently {self.stance}.')
        for stanceKey, stanceValue in stanceList[self.stance].items():
            print(f'{stanceKey}: {stanceValue}')

    def changeStance(self, newStance) -> None:
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

class Brujadha(Character):
    def __init__(self, name: str, race: str) -> None:
        super().__init__(name, race)
    def castSpell(self, target):
        #FIXME: describe logic for spells
    
