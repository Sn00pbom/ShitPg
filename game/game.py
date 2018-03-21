
import input

#PRIMARY GAME LOOP AND GLOBAL VARIABLES ASSUMING CORRECT STATE LOADED

# Initialize the scenario (done first time do is ran)
# Check for buffs/debuffs/actions
# Allow turn execution
# Transfer turn
#kk
party = None
scenario = None

def game_loop(scen):
    running = True
    scenario = scen
    print "dba"
    while running:
        scenario = scenario.do()
        if scenario == None:
            running = False
    input.delay_print('Exiting game..........................')