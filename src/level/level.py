from src.classes import *
from src.monsters import *
class Level:
    subLevels = [] ##Level array can be appended check for sublevels
    # players = [] ##array of Instantiated classes
    # monsters = []#array of monsters

    def __init__(self,name,players,monsters):
        self.name = name
        self.players = players
        self.monsters = monsters
        print "db init"

    def doRound(self):
        print "db roundstart"
        for player in self.players:
            print player.name

        #player array loop turns
        for player in self.players:
            if player.isAlive():
                player.doTurn(self.monsters)

            self.doAllTurnTicks()#poisoneffects etc

        #monster array loop turns
        for monster in self.monsters:
            if monster.isAlive():
                monster.doTurn(self.players)
            self.doAllTurnTicks()#poisoneffects etc

        #end of round effects
        self.doAllRoundEndTicks()
        print "db roundend"

    def anyPlayersAlive(self):

        for player in self.players:
            if player.isAlive():
                return True
        print "Party has wiped!"
        return False
    def anyMonstersAlive(self):
        for monster in self.monsters:
            if monster.isAlive():
                return True
        print self.name + " cleared! Proceeding..."
        return False

    def doAllTurnTicks(self):
        for player in self.players:
            player.doTurnTick()
        for monster in self.monsters:
            monster.doTurnTick()
    def doAllRoundEndTicks(self):
        for player in self.players:
            player.doRoundEndTick()
        for monster in self.monsters:
            monster.doRoundEndTick()

def doLevel(level):
    if not level.subLevels:#check if level has sublevels or "phases"
        print "db nosub"
        while level.anyPlayersAlive() and level.anyMonstersAlive():
            level.doRound()

    else:
        for subLevel in level.subLevels:
            doLevel(subLevel)
        print "db hassub"


