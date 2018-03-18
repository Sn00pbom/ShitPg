# from game.input.controlledinput import ControlledInput
from game import input

class TravelNode(object):


    # name = "TravelNode"
    # nodes = []
    def __init__(self,name,behavior):
        self.name = name
        self.nodes = [] #NODES MUST BE INIT LATER
        self.prop1 = 0
        self.prop2 = 0
        self.prop3 = 0
        self.prop4 = 0
        self.prop5 = 0
        self.prop6 = 0
        self.behavior = behavior
        #these node properties can modify behavior on a given node's

    #

    def choose(self):  #some action or prompt before movement

        self.behavior(self)
        input.delay_print("\n"
                          "Where to go....?")
        self.printConnected()

        choice = input.selectFromList(self.nodes)  # node object handle
        print ""
        choice.choose()

    def printConnected(self):
        for x in range(0,len(self.nodes)):
            input.delay_print(str(x+1) +  " "+ self.nodes[x].name)

    # def choose(self):
    #
    #     choice = controlledinput.selectFromList(self.nodes) #node object handle
    #     choice.choose()




def goToNode(node):
    node.choose()