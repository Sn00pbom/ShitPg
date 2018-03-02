
from ..classes import *
from ..monsters import *
from level import Level


def level1():
    players = []

    players.append(Mage("Player1",40,100))
    players.append(Rogue("Player2",50))

    monsters = []


    for i in range(0,5):
        monsters.append(Basicbitch("BB"+str(i+1),11))

    print "db " + str(players)
    level = Level("Level1")
    level.players = players
    level.monsters = monsters
    return level
def levelSubDummy():
    players = []
    players.append(Dummy("Dum1", 15))
    players.append(Dummy("Dum2", 20))
    monsters = []
    monsters.append(Basicbitch("Basic Bitch", 15))
    monsters.append(Basicbitch("Basic Bitch", 15))
    monsters.append(Basicbitch("Basic Bitch", 20))
    level = Level("LevelwSub")
    levels1 = Level("Phase1")
    levels1.players = players
    levels1.monsters = monsters
    monsters.append(Basicbitch("bb4:",30))
    levels2 = Level("Phase2")
    levels2.players = players
    levels2.monsters = monsters

    level.subLevels.append(levels1)
    level.subLevels.append(levels2)
    return level

def levelDummy():
    players = []
    players.append(Dummy("Dum 1",15))
    players.append(Dummy("Dum 2",20))
    players.append(Dummy("Dum 3", 20))
    players.append(Dummy("Dum 4", 20))
    monsters = []
    monsters.append(Basicbitch("Basic Bitch", 15))
    monsters.append(Basicbitch("Basic Bitch", 15))
    monsters.append(Basicbitch("Basic Bitch", 15))
    level = Level("DummyLevel")
    level.players = players
    level.monsters = monsters
    return level
