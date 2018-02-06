
class Entity(object):
    def __init__(self,name,hp):
        self.alive = True
        self.stunned = False
        self.name = name
        self.hp = hp




    def isAlive(self):
        return self.alive

    def damage(self,attacker,damage):
        if(damage >= self.hp):
            self.hp = 0
            self.alive = False
        else:
            self.hp = self.hp - damage
    def printHP(self):
        print(self.hp)




