from src.player import Player

from src.monsters.basicbitch import Basicbitch
from src.entity import Entity
from src.level import *
import random

from classes.convert import convertToClass
from classes.mage import Mage
def dummy():
    level.doLevel(leveldef.levelDummy())
def go1():
    level.doLevel(leveldef.level1())
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


print("anus IS ANUS")

# go()
# go1()
dummy()