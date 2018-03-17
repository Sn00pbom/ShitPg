import travelnode
from w1_2 import w1_2

#first location player spawns in
class w1_1(travelnode.TravelNode):
    name = "The beginning..."
    nodes = [w1_2]
    choose = travelnode.TravelNode.choose()

    # super(self.__class__,self).__init__(name,nodes)
