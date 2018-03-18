

import game.world as world

from game.item.items import Items
from game.level import level
from game.level.leveldef import *
from game.player import Player
from game.monsters.basicbitch import Basicbitch
from game.entity import Entity
from game.input import controlledinput

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
def mainMenu():
    printTitle()
    delay_print("1: Begin game\n2: Save\n3: Load\n4: Quit")
    inp = controlledinput.getIn(['1', '2', '3', '4'])
    if inp == '1':
        world.goToNode(world.Nodes.b_1)
        # dummy(running)
    elif inp == '4':
        delay_print("Quitting................")
        sys.exit()
    elif inp == '2':
        # save
        pass
    elif inp == '3':
        # load
        pass


running = True


def primaryLoop():

    while running:
        #do shit

        mainMenu()




# primaryLoop()
weapon = Items.BONE_KNIFE
weapon2 = Items.BONE_FRAGMENT

print weapon.name
print weapon2.name

world.goToNode(world.Nodes.b_2)

# dummysub()
