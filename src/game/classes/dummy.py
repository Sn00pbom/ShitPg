
import random

from ..player import Player
from ..entity import Entity

from ..input.controlledinput import *
from ..input.cmdinterface import *

class Dummy(Player):
    target = Entity("db", 1)

    def doTurn(self,monsters):
        super(Dummy,self).doTurn(monsters)

        # print "Choose target to punch"
        delay_print("Choose target to punch")

        printEntitiesInList(monsters)
        self.punch(selectFromList(monsters))




    def punch(self,monster):
        monster.damage(self,4)
        delay_print("POW!........................................")

