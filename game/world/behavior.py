from game import input
from game.input.cmdinterface import delay_print as dprint
from game.scenario import scenariolevel
from game.scenario import leveldef
from game.scenario import ScenarioMenu
import pyfiglet
from game import game

#these must always have travelnode as parameter
def nobeh(travelnode=None):
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
            print pyfiglet.figlet_format("(  .  )(  .  )", input.FONT_ALLIGATOR)
            return ScenarioMenu("Main")


    def norape():
        dprint("You remember being woken here unpleasantly...")

    if travelnode.prop["prop1"] == 0:
        rape()
    elif travelnode.prop["prop2"] == 1:
        norape()




def behw1_2(travelnode):

    print "this is custom behavior on b_2 node"

def behw1_2_2(travelnode):

    # scenariolevel.doLevel(leveldef.levelDummy())
    if travelnode.prop1 == 0:
        #fight

        input.delay_print("You're caught off gaurd by some Basic Bitches.......\n")
        input.delay_print("db")
        input.delay_print(pyfiglet.figlet_format("Fight",input.FONT_ALLIGATOR),sleep=0.002)
        travelnode.prop1 = 1 #fight no rerun
        return leveldef.levelDummy()


all = {#put all function definitions in the dictionary
    "nobeh":nobeh,
    "beh1":behw1_1,
    "beh2":behw1_2,
    "beh3":behw1_2_2
}
