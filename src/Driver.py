from src.Player import Player

from src.monsters.Basicbitch import Basicbitch

from classes.Convert import convertToClass
from classes.Mage import Mage
def go():
    print "go"
    player = Player("bitch",10)
    monster = Basicbitch("bb1",10)

    newmage = Mage("bitch",1000,300)
    print isinstance(newmage,Mage)

    newmage.fireball(monster)
    monster.printHP()
    print type(monster)
    mage = convertToClass(player,Mage)
    print mage.hasMP(10)
    mage.fireball(monster)
    monster.printHP()



    print(type(player) is Player)
    print type(player)

    print type(Player)

    # print("hello" + isinstance(player, Player))
    print(isinstance(player, Player))

    if type(player) == Player:
        print "ih"


print("anus IS ANUS")

go()
