from src.classes import *
from src.monsters import *
from src.level.level import Level
def level1():
    players = []

    players.append(Mage("Player1",40,100))
    players.append(Rogue("Player2",50))

    monsters = []

    for i in range(0,5):
        monsters.append(Basicbitch("BB"+str(i+1),11))

    print "db " + str(players)

    return Level("Level1",players,monsters)
def levelDummy():
    players = []
    players.append(Dummy("Dum1",15))
    players.append(Dummy("Dum2",20))
    monsters = []
    monsters.append(Basicbitch("bb1",15))
    monsters.append(Basicbitch("bb1", 15))
    monsters.append(Basicbitch("bb1", 15))
    return Level("DummyLevel",players,monsters)
