from entity import Entity

class Player(Entity):
    target = None


    def doTurn(self,enemies):
        #get inputs
        print "db player turn"
    def doTurnTick(self):
        # print "db player self turn tick"
        pass
    def doRoundEndTick(self):

        print "db player round end"