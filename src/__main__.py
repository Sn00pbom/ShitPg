



from game.level import level
from game.level.leveldef import *
from game.player import Player
from game.monsters.basicbitch import Basicbitch
from game.entity import Entity




from game.input.controlledinput import *

import getch


def dummysub():

    level.doLevel(levelSubDummy())
def dummy(running):

    level.doLevel(levelDummy())
    running = False
def go1():
    level.doLevel(level1())
def go():
    print "go"


    player = Player("bitch",10)
    monster = Basicbitch("bb1",10)

    if isinstance(monster,Entity):
        print "db monster entity"



    print(type(player) is Player)
    print type(player)

    print type(Player)

    # print("hello" + isinstance(player, Player))
    print(isinstance(player, Player))

    if type(player) == Player:
        print "ih"
#new testcommit
# go()
# go1()

# print controlledIn(['1','2','3'])
# print getIn(['1','2','3','4'])
# testGetch()
def gameLoop():
    running = True
    while running:
        #do shit
        printTitle()

        dummy(running)



gameLoop()

# dummysub()