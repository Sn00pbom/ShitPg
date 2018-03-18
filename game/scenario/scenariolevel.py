from game import input
from scenariomenu import ScenarioMenu

class ScenarioLevel(object):
    subLevels = [] ##Level array can be appended check for sublevels
    players = [] ##array of Instantiated classes
    monsters = []#array of monsters

    def __init__(self,name):
        self.name = name


    def do(self):
        print "db roundstart"

        #player array loop turns
        for player in self.players:
            if player.canAct():
                player.doTurn(self.monsters)
            else:
                if player.isAlive():
                    print player.name + " is stunned!"
                else:
                    print player.name + " isn't breathing..."


            self.doAllTurnTicks()#poisoneffects etc

        #monster array loop turns
        for monster in self.monsters:
            if monster.isAlive():
                monster.doTurn(self.players)
            self.doAllTurnTicks()#poisoneffects etc

        #end of round effects
        self.doAllRoundEndTicks()
        print "db roundend"


        if self.anyPlayersAlive() == False:
            return None
        elif self.anyMonstersAlive() == False:
            return ScenarioMenu("MainMenu")
        return self

    def anyPlayersAlive(self):

        for player in self.players:
            if player.isAlive():
                return True
        input.delay_print("Party has wiped!")
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
    # def updateMonsters(self):
    #     updated = []
    #     for monster in self.monsters:
    #         if monster.isAlive():
    #             updated.append(monster)
    #     self.monsters = updated

def doLevel(level):
    if not level.subLevels:#check if scenario has sublevels or "phases"
        print "db nosublevel beginning scenario..."

        while level.anyPlayersAlive() and level.anyMonstersAlive():
            level.doRound()

    else:
        print "db hassublevel"
        print level.subLevels
        for subLevel in level.subLevels:
            print "db subleveldo"
            doLevel(subLevel)



