from src.player import Player
from src.entity import Entity
import random
class Dummy(Player):
    target = Entity("db", 1)

    def doTurn(self,monsters):
        print "db dummyturn"
        self.punch(self.selectTarget(monsters,True))
    def selectTarget(self, monsters, rand):
        if rand:
            targetint = random.randint(0, len(monsters)-1)
            self.target = monsters[targetint]
            entity = self.target
            entity.printHP()
            return entity

    def punch(self,monster):
        monster.damage(self,4)