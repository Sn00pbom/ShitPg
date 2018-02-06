
import random

from ..player import Player
from ..entity import Entity

from ..input.controlledinput import *
from ..input.cmdinterface import *

class Dummy(Player):
    target = Entity("db", 1)

    def doTurn(self,monsters):
        print "db dummyturn " + self.name
        print "Choose target to punch"
        printEntityiesInList(monsters)
        self.punch(selectFromList(monsters))


    def selectTarget(self, monsters, rand):
        if rand:
            targetint = random.randint(0, len(monsters)-1)
            self.target = monsters[targetint]
            entity = self.target
            entity.printHP()
            return entity

    def punch(self,monster):
        monster.damage(self,4)

