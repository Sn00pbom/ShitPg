from game import input
class ScenarioTravel(object):

    def __init__(self,name):
        self.name = name

    def do(self):
        #game loop root
        input.delay_print("Travel Scenario........")
        return self
