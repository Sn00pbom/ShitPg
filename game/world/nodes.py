from travelnode import TravelNode as tn
from behavior import *
#these are global references for the nodes. must init after

class Nodes():

    #define nodes
    b_1 = tn("The Beginning",behw1_1)
    b_2 = tn("An Empty Area in the woods.",behw1_2)
    b_2_1 = tn("???",nobeh)
    b_2_2 = tn("An Area with a well...",behw1_2_2)



    #define connected nodes
    b_1.connect(E=b_2)
    b_2.connect(W = b_1,S=b_2_1,UP=b_1)
    b_2_1.connect(DOWN=b_2_2)
    b_2_2.connect(DOWN=b_1)