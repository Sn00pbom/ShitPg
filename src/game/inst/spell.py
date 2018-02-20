
class Spell():
    def __init__(self,name,costType,cost):
        self.name = name
        self.costType = costType
        self.cost = cost

def fireball(self,entity):
    print "db fireball"
    entity.damage(self,5)