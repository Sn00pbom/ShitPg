
import input

#PRIMARY GAME LOOP AND GLOBAL VARIABLES ASSUMING CORRECT STATE LOADED

# Initialize the scenario (done first time do is ran)
# Check for buffs/debuffs/actions
# Allow turn execution
# Transfer turn
#kk


def game_loop(scenario):
    running = True
    while running:
        scenario = scenario.do()
        if scenario == None:
            running = False
    input.delay_print('Exiting game..........................')