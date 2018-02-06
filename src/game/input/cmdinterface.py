from ..entity import Entity

def printEntityiesInList(entities):
    i = 0

    for e in entities:
        print str(i+1) + " " + e.name
        print "  HP: " + str(e.hp)
        i+= 1
