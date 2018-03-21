# from game.input.controlledinput import ControlledInput
from game import input
from game import game

class TravelNode(object):


    # name = "TravelNode"
    # nodes = []
    E = None
    NE = None
    N = None
    NW = None
    W = None
    SW = None
    S = None
    SE = None
    UP = None
    DOWN = None




    def __init__(self,name,behavior):
        self.name = name

        #now using Direction class
        #[E,NE,N,NW,W,SW,S,SE,UP,DOWN] node positions
        # self.nodes = [None,None,None,None,None,None,None] #NODES MUST BE INIT LATER
        self.revealed = False

        self.prop1 = 0
        self.prop2 = 0
        self.prop3 = 0
        self.prop4 = 0
        self.prop5 = 0
        self.prop6 = 0
        self.behavior = behavior
        #these node properties can modify behavior on a given node's

    #

    def connected(self):
        out = []
        if self.E != None: out.append(self.E)
        if self.NE != None: out.append(self.NE)
        if self.N != None: out.append(self.N)
        if self.NW != None: out.append(self.NW)
        if self.W != None: out.append(self.W)
        if self.SW != None: out.append(self.SW)
        if self.S != None: out.append(self.S)
        if self.SE != None: out.append(self.SE)
        if self.UP != None: out.append(self.UP)
        if self.DOWN != None: out.append(self.DOWN)
        return out

    # def getDirectionFromNode(self,node):
    #     if self.E == node: return "Go East"
    #     if self.NE == node: return "Go NorthEast"
    #     if self.N == node: return "Go North"
    #     if self.NW == node: return "Go NorthWest"
    #     if self.W == node: return "Go West"
    #     if self.SW == node: return "Go SouthWest"
    #     if self.S == node: return "Go South"
    #     if self.SE == node: return "Go SouthEast"
    #     if self.UP == node: return "Ascend"
    #     if self.DOWN == node: return "Descend"
    #     return "None"
    def getDirectionsFromNode(self,node):
        out = []
        if self.E == node: out.append("Go East")
        if self.NE == node: out.append("Go NorthEast")
        if self.N == node: out.append("Go North")
        if self.NW == node: out.append("Go NorthWest")
        if self.W == node: out.append("Go West")
        if self.SW == node: out.append("Go SouthWest")
        if self.S == node: out.append("Go South")
        if self.SE == node: out.append("Go SouthEast")
        if self.UP == node: out.append("Ascend")
        if self.DOWN == node: out.append("Descend")
        if len(out) == 0: #no nodes connected
            return "None"
        elif len(out) == 1:
            return out[0] #only 1
        else:
            return out #multiple copy nodes connected to same central node



    def do(self):  #some action or prompt before movement
        input.delay_print("\nEntered " + self.name + " --/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        # input.delay_print("\nEntered " + self.name + "................................................................")
        self.revealed = True #once the player travels to the given node, it becomes revealed in map decisions
        game.party.setNode(self)
        newScenario = self.behavior(self)
        if newScenario != None:
            return newScenario


        input.delay_print("\n"
                          "Where to go....?")
        self.printConnected()

        choice = input.selectFromList(self.connected())  # node object handle
        if choice == None:
            input.delay_print("You have no where to go........................\n"
                              "The party dies.................\n"
                              "Game Over\n"
                              "\n"
                              "\n")
        # choice.choose()
        return choice



    def printConnected(self):
        nodes = self.connected()
        used = 0 ##prevents printing the same direction when the destinations are the same
        for x in range(0,len(nodes)):
            node = nodes[x]

            dirs = self.getDirectionsFromNode(node)

            if type(dirs) == list:
                if node.revealed == True:
                    input.delay_print(
                        str(x + 1) + ": " + self.getDirectionsFromNode(node)[used] + " to " + nodes[x].name)
                else:
                    input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node)[used])
                used += 1
            else:
                if node.revealed == True:
                    input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node) + " to " + nodes[x].name)
                else:
                    input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node))

    def revealAll(self):
        for node in self.connected():
            node.revealed = True

    def connect(self,E=None,NE=None,N=None,NW=None,W=None,SW=None,S=None,SE=None,UP=None,DOWN=None):
        if E: self.E = E
        if NE: self.NE = NE
        if N: self.N = N
        if NW: self.NW = NW
        if W: self.W = W
        if SW: self.SW = SW
        if S: self.S = S
        if SE: self.SE = SE
        if UP: self.UP = UP
        if DOWN: self.DOWN = DOWN





