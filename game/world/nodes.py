from travelnode import TravelNode
from behavior import *
#these are global references for the nodes. must init after

class Nodes():

    #define nodes
    b_1 = TravelNode("The Beginning",behw1_1)
    b_2 = TravelNode("An Empty Area in the woods.",behw1_2)
    b_2_1 = TravelNode("???",nobeh)



    #define connected nodes
    b_1.nodes = [b_2]
    b_2.nodes = [b_1,b_2_1]
    b_2_1.nodes = [b_2]