from ..classes import *

# from mage import Mage


def convertToClass(entity, classtype):


    if classtype == Mage:
        print "db ismage"
        newMage = Mage(entity.name, entity.hp, 100)
        return newMage
    elif classtype == Rogue:
        return Rogue(entity.name, entity.hp)

