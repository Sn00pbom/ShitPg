from game import input

class ScenarioMenu(object):

    def __init__(self,name):
        # self.option
        self.name = name

    def do(self):
        #game loop root
        input.delay_print("THIS IS THE MAIN MENU...........................")
        return self

    # def mainMenu():
    #     printTitle()
    #     delay_print("1: Begin game\n2: Save\n3: Load\n4: Quit")
    #     inp = controlledinput.getIn(['1', '2', '3', '4'])
    #     if inp == '1':
    #         dummy(running)
    #     elif inp == '4':
    #         delay_print("Quitting................")
    #         sys.exit()
    #     elif inp == '2':
    #         # save
    #         pass
    #     elif inp == '3':
    #         # load
    #         pass
