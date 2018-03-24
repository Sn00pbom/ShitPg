# from game.input.controlledinput import ControlledInput
from game import input
from game import game
from game.world import behavior

class TravelNode(object):


    # name = "TravelNode"
    # nodes = []
    # E = None
    # NE = None
    # N = None
    # NW = None
    # W = None
    # SW = None
    # S = None
    # SE = None
    # UP = None
    # DOWN = None




    def __init__(self,nodeDef,zonename,rawname):
        # playerdata fields
        self.prop = {"revealed": False}  # every node must have revealed property, starts at false until changed

        # definition fields
        try:
            self.name = nodeDef["name"]  # display name
            self.zonename = zonename
            self.rawname = rawname  # generated from load dic path
            self.behavior = behavior.all[nodeDef["behavior"]]  # link to function def in behavior module
            self.connected = nodeDef["connected"]
            try:
                for key in nodeDef["properties"]:
                    self.prop[key] = nodeDef["properties"][key]
            except:
                pass  # no properties field found in node definition


        except:
            print "Node definition loading failed... exiting..."
            exit(0)



    def do(self):  #some action or prompt before movement
        input.delay_print("\nEntered " + self.name + " --/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        # input.delay_print("\nEntered " + self.name + "................................................................")
        self.prop["revealed"] = True #once the player travels to the given node, it becomes revealed in map decisions
        game.scenario = self
        newScenario = self.behavior(self)
        if newScenario != None:
            return newScenario


        input.delay_print("\n"
                          "Where to go....?")
        self.printConnected()

        choice = input.selectFromList(self.getConnected())  # node object handle
        if choice == None:
            input.delay_print("You have no where to go........................\n"
                              "The party dies.................\n"
                              "Game Over\n"
                              "\n"
                              "\n")
        # choice.choose()
        return choice

    def getConnected(self):
        out = []
        for key in self.connected:
            out.append(self.connected[key])
        return out

    def printConnected(self):
        choice = 1
        # nodes = self
        # used = 0 ##prevents printing the same direction when the destinations are the same
        # for x in range(0,len(nodes)):
        #     node = nodes[x]
        #
        #     dirs = self.getDirectionsFromNode(node)
        #
        #     if type(dirs) == list:
        #         if node.revealed == True:
        #             input.delay_print(
        #                 str(x + 1) + ": " + self.getDirectionsFromNode(node)[used] + " to " + nodes[x].name)
        #         else:
        #             input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node)[used])
        #         used += 1
        #     else:
        #         if node.revealed == True:
        #             input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node) + " to " + nodes[x].name)
        #         else:
        #             input.delay_print(str(x + 1) + ": " + self.getDirectionsFromNode(node))
        for key in self.connected:
            toNode = self.connected[key]
            if toNode.prop["revealed"] == True:
                print str(choice) + ": " + key + " towards " + toNode.name
            else:
                print str(choice) + ": " + key
            choice += 1

    def revealAll(self):
        for node in self.connected():
            node.revealed = True




