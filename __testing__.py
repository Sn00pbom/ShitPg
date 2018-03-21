

from game import scenario
from game.player import Player
from game.monsters.basicbitch import Basicbitch
from game.entity import Entity
from game import game
from game import world
from game.item.items import Items

from game.party import Party



# primaryLoop()
weapon = Items.BONE_KNIFE
weapon2 = Items.BONE_FRAGMENT

print weapon.name
print weapon2.name


tr1 = world.TravelNode("test1",world.nobeh)

tr2 = world.TravelNode("test2",world.nobeh)
tr3 = world.TravelNode("test3",world.behw1_2_2)

tr1.connect(E=tr2)
tr2.connect(W=tr1,UP=tr3)

# tr3.prop1 = 1 #prevents fight scene
tr3.connect(DOWN=tr1)

party = Party()
party.addDummyMembers()
party.setNode(tr1)
game.party = party
game.game_loop(tr1)