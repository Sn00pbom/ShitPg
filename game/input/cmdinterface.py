from ..entity import Entity
import time
import sys
import pyfiglet
# from ..util import imgtoshell

FONT_GRAFFITI = 'graffiti'
FONT_METAL = 'amcrazor'
FONT_ALLIGATOR = 'alligator'


def delay_print(s,newline = None,sleep = 0.01): #prints a string progressively. can be used as a "wait timer" between actions by using ............
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c is not " ": time.sleep(sleep) #doesnt wait on space print


    if newline is None or newline: print "" #prints a newline given argument



# def delay_print(s,newline):
#     for c in s:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(0.01)
#     if newline: print "" #prints a newline given argument

def printEntitiesInList(entities):
    i = 0

    for e in entities:
        delay_print(str(i+1) + ": " + e.name)
        delay_print("  HP: " + str(e.hp))
        # print str(i+1) + " " + e.name
        # print "  HP: " + str(e.hp)
        i += 1

def printStringList(list):
    i = 0

    for e in list:
        delay_print(str(i + 1) + ": " + e)

        i += 1

def printTitle():
    title = """\
    #######################################################
         _________.__    .__  __ __________  ________
        /   _____/|  |__ |__|/  |\______   \/  _____/
        \_____  \ |  |  \|  \   __\     ___/   \  ___
        /        \|   Y  \  ||  | |    |   \    \_\  |
       /_______  /|___|  /__||__| |____|    \______  /
               \/      \/                          \/ 
    #######################################################
    """
    delay_print(title)
    # delay_print(pyfiglet.figlet_format("ShitPG",font='graffiti'))
    # imgtoshell.convertAndPrint('./game/shitpg.bmp')
