from src.monsters.monster import Monster
class Basicbitch(Monster):
    anger = 5


    def rageHeal(self):
        if self.anger >10:
            self.hp += 7

    def doTurn(self,players):
        print "db bb turn"
        self.cuntScream(players)

    def cuntScream(self,players):
        for player in players:
            player.damage(self,1)