from ..player import Player

class Mage(Player):

    def __init__(self,name,hp,mp):
        self.name = name
        self.hp = hp
        self.mp = mp


    def fireball(self,entity):
        print "db fireball"
        entity.damage(self,5)

    def hasMP(self,amount):
        if amount>self.mp:
            return False
        else:
            return True