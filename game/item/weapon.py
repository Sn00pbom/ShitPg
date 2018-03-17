from item import Item

class Weapon(Item):

    def __init__(self,name):
        super(Weapon,self).__init__(name) #super class constructor call
