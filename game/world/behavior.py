from game import input
from game.input.cmdinterface import delay_print as dprint
from game.level import level
from game.level import leveldef
import pyfiglet

#these must always have travelnode as parameter
def nobeh(travelnode):
    pass

def behw1_1(travelnode):
    def rape():
        dprint("You've woken up in the woods. You're being raped by some boars.......\n" \
                          "Press 1 to punch the boars and knock them out............")

        input.printStringList(["Punch Boars in da mouf","Do nuffin"])
        choice = input.selectFromList([1,2])
        if choice == 1:
            dprint("The Boars drop dead, and turn instantly to dust.......")
            travelnode.prop1 = 1
        elif choice == 2:
            dprint("The Boars continue to relentlessly rape you in the bum.\n"
                   ".............\n"
                   "You've decided to do nothing. Your bum hurts.\n"
                   "................\n"
                   "You die from bum rape")
            print pyfiglet.figlet_format("(  .  )(  .  )", font='alligator')
            exit()


    def norape():
        dprint("You remember being woken here unpleasantly...")

    if travelnode.prop1 == 0:
        rape()
    elif travelnode.prop1 == 1:
        norape()




def behw1_2(travelnode):
    print "this is custom behavior on b_2 node"

def behw1_2_2(travelnode):
    level.doLevel(leveldef.levelDummy())