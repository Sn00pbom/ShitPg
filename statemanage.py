import os
import json
from game.world.travelnode import TravelNode
from game import game

def loadTravelNodeDefs():
    # this will
    # A: read all nodes found in all files in the locs folder,
    # B: take all nodes and put their values into a dictionary,
    # C: create correct connections in every node found in dictionary
    # D: connect nodes to each other globally

    # A
    datas = []  # array of data from files
    jsloads = []  # array of json loaded files
    folder = "./data/loc/"  # node definition folder
    for fileName in os.listdir(folder):  # for every file name found in the locations folder
        load = open(folder + fileName, "r")
        datas.append(load)  # opens data as read

    # B
    for data in datas:  # for every data found in the opened array
        load = json.load(data)
        jsloads.append(load)
    # C
    for jsload in jsloads:
        for zoneKey in jsload:  # loops through all zoneKeys found
            for nodeKey in jsload[zoneKey]:  # loops through all nodeKeys found
                rawname = zoneKey + "." + nodeKey
                newTravelNode = TravelNode(jsload[zoneKey][nodeKey],zoneKey,rawname)  # passes nodeKey values and rawname to node object
                game.nodes[newTravelNode.rawname] = newTravelNode  # puts node object in global dict
    #D
    for globalTravelNodeKey in game.nodes:  # forms all relative node connection
        for directionKey in game.nodes[globalTravelNodeKey].connected:
            node = game.nodes[globalTravelNodeKey]  # this iterations node
            targetRaw = node.connected[directionKey]
            if "." not in targetRaw:#target raw is in same world
                targetRaw = node.zonename + "." + targetRaw #updates in world target raw to hit correct global dictionary def

            node.connected[directionKey] = game.nodes[targetRaw]  # takes direction key W N S etc and sets it's value to the rawname value

def loadTravelNodePlayerdata(fileName):
    # this will
    # A: read all game.nodes found in all files in the saves folder,
    # B: take all game.nodes and put their values into a dictionary,
    # C: create correct connections in every node found in dictionary
    # D: connect game.nodes to each other globally

    # A
    datas = []  # array of data from files
    jsloads = []  # array of json loaded files
    folder = "./data/save/"  # node definition folder
    path = folder + fileName
    # for fileName in os.listdir(folder):  # for every file name found in the locations folder
    #     load = open(folder + fileName, "r")
    #     datas.append(load)  # opens data as read
    jsload = json.load(open(path))
    # B
    # for data in datas:  # for every data found in the opened array
    #     load = json.load(data)
    #     jsloads.append(load)
    # C
    # for jsload in jsloads:#loops all loads
    for rawname in jsload["loc"]:
        node = game.nodes[rawname]
        for propertyKey in jsload["loc"][rawname]:
            node.prop[propertyKey] = jsload["loc"][rawname][propertyKey]

    game.scenario = game.nodes[jsload["party"]["loc"]]

def printAllTravelNodes():
    for globalTravelNodeKey in game.nodes:
        print globalTravelNodeKey + " is connected to:"
        node = game.nodes[globalTravelNodeKey]
        for directionKey in node.connected:
            print "     " +directionKey + " " + node.connected[directionKey].rawname
        print "     " + globalTravelNodeKey + " properties:"
        for propertyKey in node.properties:
            # print propertyKey
            print "          " + propertyKey + " " + str(node.properties[propertyKey])

def loadAll(fileName):
    loadTravelNodeDefs()
    loadTravelNodePlayerdata(fileName)

