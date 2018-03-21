from game import input
from game import game
from game.party import Party


class ScenarioTravel(object):

    @DeprecationWarning
    def __init__(self,name):
        self.name = name
        # self.node = node
        self.inCombat = False

    @DeprecationWarning
    def do(self): #No longer using this idea, rather using only travel nodes to handle
        #game loop root
        input.delay_print("Travel Scenario........")
        print game.party.node
        game.party.node = game.party.node.choose()
        while self.inCombat:
            pass


        return self

    # def choose(self):  #some action or prompt before movement
    #
    #     self.behavior(self)
    #     input.delay_print("\n"
    #                       "Where to go....?")
    #     self.printConnected()
    #
    #     choice = input.selectFromList(self.nodes)  # node object handle
    #     print ""
    #     choice.choose()