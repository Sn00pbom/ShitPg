from game.input.controlledinput import ControlledInput

class TravelNode():


    # name = "TravelNode"
    # nodes = []
    # # def __init__(self,name,nodes):
    # #     self.name = name
    # #     self.nodes = nodes
    #

    def choose(self):
        choice = ControlledInput.selectFromList(self.nodes) #node object handle
        choice.choose()

    def goToNode(self,node):
        node.choose()




