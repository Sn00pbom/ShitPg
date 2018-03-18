from game import input
from game.input.cmdinterface import delay_print as dprint

#these must always have travelnode as parameter
def nobeh(travelnode):
    pass

def behw1_1(travelnode):
    def rape():
        dprint("You've woken up in the woods. You're being raped by some boars.......\n" \
                          "Press 1 to punch the boars and knock them out............")

        input.printStringList(["Punch Boars in da mouf"])
        input.selectFromList([1])

        dprint("The Boars drop dead, and turn instantly to dust.......")
        travelnode.prop1 = 1
    def norape():
        dprint("You remember being woken here unpleasantly...")

    if travelnode.prop1 == 0:
        rape()
    elif travelnode.prop1 == 1:
        norape()




def behw1_2(travelnode):
    print "this is custom behavior on b_2 node"
