from ..inst import spell
from ..player import Player
class Rogue(Player):


    def __init__(self,name,hp,energyMax):
        self.name = name
        self.hp = hp
        self.enerMax = energyMax
        self.energy = energyMax
        self.spells = loadRogueSpells()
def loadRogueSpells():
    print "db roguespellload"
