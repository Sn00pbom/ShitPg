import travelnode
from game.input.controlledinput import ControlledInput

class w1_1(travelnode.TravelNode):
    # this class extends the normal travelnode, and can have custom properties that are different than the original travelnode
    def __init__(self,name,nodes,property):
        super(self.__class__,self).__init__(name,nodes)
        self.property = property

    def choose(self):
        #some custom thing here. either combat engage or other choice.
        choice = ControlledInput.selectFromList(["Roll to the left","Roll to the right"])
        if choice == "Roll to the left":
            print "db left"
        elif choice == "Roll to the right":
            print "db right"


        super(self.__class__,self).choose()

