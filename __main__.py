import statemanage
from game import game

#LOAD STATES
statemanage.loadAll("save1.json")


game.game_loop(game.scenario)#run the loaded scenario