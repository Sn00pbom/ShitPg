
class Level:
    subLevels = [] ##Level array can be appended check for sublevels
    players = [] ##array of Instantiated classes
    enemies = []

    def __init__(self):
        print "db init"

    def doRound(self):
        print "db roundstart"

        #player array loop turns

        #monster array loop turns

        #end of round effects
        print "db roundend"





def startLevel(level):
    if not level.subLevels:#check if level has sublevels or "phases"
        print "db nosub"
    else:
        print "db hassub"

