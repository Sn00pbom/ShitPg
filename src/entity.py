class Entity(object):
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    alive = True

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




