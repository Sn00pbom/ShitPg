from ..player import Player
from ..inst.spell import *
class Mage(Player):

    def __init__(self,name,hp,mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.spells = loadMageSpells()




    def hasMP(self,amount):
        if amount>self.mp:
            return False
        else:
            return True

def loadMageSpells():
    spells = []
    spells.append(spell.fireball)