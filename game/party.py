import input
from classes.dummy import Dummy
import world

class Party(object):

    def __init__(self):
        self.members = []
        self.node = world.TravelNode("Detached Node", world.nobeh)



    def printMembers(self):
        number = 1
        for member in self.members:
            input.delay_print(str(number) + ": " + member.name)
            number += 1

    def addDummyMembers(self):
        self.members.append(Dummy("Dum1", 15))
        self.members.append(Dummy("Dum2", 20))
        self.members.append(Dummy("Dum2", 30))
        self.printMembers()
    def setNode(self,node):
        self.node = node
    def getNode(self):
        print "db"
        if self.node: return self.node