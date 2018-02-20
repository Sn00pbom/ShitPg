import getch

# def controlledIn(validInputs):
#     input = "db"
#     while not validInputs.__contains__(input):
#         input = getKey()
#     return input

def getIn(validInputs):
    input = ''
    while not validInputs.__contains__(input):
        input = getch.getch()
        # print input
    return input

def selectFromList(list):#type adapts, returns 1 element from list
    #DOES NOT PRINT
    #this function goes into an array input to get
    if list:
        options = []
        for x in range(0,len(list)):
            s = str(x+1)
            c = s[0]
            options.append(c)
        inp = getIn(options)
        print inp
        out = list[int(inp)-1]
        return out


# def testGetch():
#     print "press a key db"
#     key = readchar.readkey()
#     pause()
#     print key
