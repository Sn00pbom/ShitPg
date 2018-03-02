from ..player import Entity
import random
class Monster(Entity):

    target = Entity("db",1)

    def selectTarget(self,players,rand):
        if rand:
            targetint = random.randint(0, len(players-1))
            self.target = players[targetint]
            entity = self.target
            return entity
        else:
            print "db specific"
    # def doTurn(self,players):
    #     print "db monster do turn"
    #     #select spell random
    #     #select target random
    def doTurnTick(self):
        # print "db monster turn tick"
        pass
    def doRoundEndTick(self):
        # print "db monster round end"
        pass