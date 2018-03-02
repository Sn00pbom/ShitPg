import costtype
from ..classes import Mage

class Spell():
    def __init__(self,name,func,costType,cost,entityType):
        self.name = name
        self.func = func
        self.costType = costType
        self.cost = cost
        self.entityType = entityType

    def run(self):
        return self.func()
        



#---------------------------SPELL FUNCTIONS

def fireball(self,entity):
    print "db fireball"
    entity.damage(self,5)

#---------------------------SPELL DEFINITIONS
all_spells = []

SPELL_FIREBALL = Spell("Fireball",fireball,costtype.MP,10,Mage)

