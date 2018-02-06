from monster import Monster
class Basicbitch(Monster):
    anger = 5


    def rageHeal(self):
        if self.anger >10:
            self.hp += 7

    def doTurn(self,players):
        print "db bb turn"
        self.cuntScream(players)

    def cuntScream(self,players):
        damage = 2
        print self.name + " used cuntscream! It hit all players for " + str(damage)
        for player in players:
            player.damage(self,4)