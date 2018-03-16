
class Entity(object):
    def __init__(self,name,hp):
        self.alive = True
        self.canact = True
        self.name = name
        self.hp = hp
        self.inventory = []
        self.spells = []
        self.effectlist = []
        self




    def doTurn(self,opponents):
        self.announce()

        #select spell player input

        #select target
    def announce(self):
        print self.name + "'s turn..."
    def isAlive(self):
        return self.alive
    def canAct(self): #should NEVER return true while player dead
        return self.canact
    def damage(self,attacker,damage):
        if(damage >= self.hp):
            self.hp = 0
            self.alive = False
        else:
            self.hp = self.hp - damage
    def printHP(self):
        print(self.hp)




