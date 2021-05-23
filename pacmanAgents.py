# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#import Queue as qlib
from pacman import Directions
from game import Agent
from heuristics import *
import random
import sys
import time

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class OneStepLookAheadAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(admissibleHeuristic(state), action) for state, action in successors]
        # get best choice
        bestScore = min(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        visited = []
        actionstochild = []
        fringe = []
        #global visitedglobaldfs
        #visitedglobaldfs += [state]
        fringe.append((0, state, actionstochild, sys.maxint))
        flag = 0
        while fringe:
            #print("len of fringe")
            #print(len(fringe))
            depth, curr_state, actionstocurr, huescore = fringe.pop(0)
            visited = visited + [curr_state]

            if curr_state.isWin():
                return actionstocurr[0]

            legal = curr_state.getLegalPacmanActions()

            successors = [(curr_state.generatePacmanSuccessor(action), action) for action in legal]
            for successor in successors:
                #print((successor[0]))
                if not successor[0]:
                    #print(successor[0])
                    #print("No succ")
                    flag = 1
                    break
                #print(successor[0])
                #time.sleep(100)
                succ_state = successor[0]
                succ_action = actionstocurr + [successor[1]]
                succ_depth = len(succ_action)
                succ_score = admissibleHeuristic(succ_state)
                #print("------------------------------------")
                #print(succ_score)


                #if succ_state not in visited and succ_state not in visitedglobaldfs:

                if succ_state.isWin():
                    return succ_action[0]
                fringe.append([succ_depth, succ_state, succ_action, succ_score])

            if flag:
                break
            #when will it come out of the while loop:
            # 1. When generatePacmanSuccessor gives none
            # 2. When fringe is empty
        if fringe:
            scored = [(succ_action[0], cost) for succ_depth, statee, succ_action, cost in fringe]
            bestScore = min(scored)[1]
            bestActions = [pair[0] for pair in scored if pair[1] == bestScore]
                #print(random.choice(bestActions))
            return random.choice(bestActions)

#visitedglobaldfs = []

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts

    #fringe will contain: depth, state, path, visited


    def registerInitialState(self, state):

        #change parameters ---> add score
        # each item in fringe contains the following elements:
        # ---------- depth, state, actionstogethere, loacl visited
        return;



    # GetAction Function: Called with every frame
    def getAction(self, state):

        actionstochild = []
        fringe = list()
        cost = admissibleHeuristic(state)
        fringe.append((0, state, actionstochild, cost))

        while fringe:
            depth, curr_state, actionstocurr, huescore = fringe.pop()

            if curr_state.isWin():
                return actionstocurr[0]

            legal = curr_state.getLegalPacmanActions()
            successors = [(curr_state.generatePacmanSuccessor(action), action) for action in legal]

            for successor in successors:
                # 1. successor is win state
                # 2. successor is none
                # 3. successor is isLose
                # successor is normal
                succ_state = successor[0]
                succ_action = actionstocurr + [successor[1]]


                if succ_state is None or succ_state.isLose():
                    scored = [(succ_action, cost) for succ_depth, statee, succ_action, cost in fringe]
                    if scored:
                        bestScore = min(scored)[1]
                        bestActions = [pair[0] for pair in scored if pair[1] == bestScore]
                        bestaction = random.choice(bestActions[0])
                    elif actionstocurr:
                        bestaction = actionstocurr[0]
                    else:
                        continue
                    #print(bestaction)
                    return bestaction

                elif succ_state.isWin():
                    return succ_action[0]

                #if it is neither win nor lose just add to stack
                succ_depth = len(succ_action)
                succ_score = admissibleHeuristic(succ_state)
                fringe.append([succ_depth, succ_state, succ_action, succ_score])






















class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    #global expanded = []

    def registerInitialState(self, state):
        expanded = []

        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        actionstochild = []
        fringe = list()
        cost = admissibleHeuristic(state) + 0
        fringe.append((0, state, actionstochild, cost))

        while fringe:
            depth, curr_state, actionstocurr, huescore = fringe.pop(0)

            if curr_state.isWin():
                return actionstocurr[0]

            legal = curr_state.getLegalPacmanActions()
            successors = [(curr_state.generatePacmanSuccessor(action), action) for action in legal]
            for successor in successors:
                    # 1. successor is win state
                    # 2. successor is none
                    # 3. successor is isLose
                    # successor is normal
                succ_state = successor[0]
                succ_action = actionstocurr + [successor[1]]


                if succ_state is None or succ_state.isLose():
                    scored = [(frin_action, cost) for frin_depth, statee, frin_action, cost in fringe]
                    if scored:
                        bestScore = min(scored)[1]
                        bestActions = [pair[0] for pair in scored if pair[1] == bestScore]
                        bestaction = random.choice(bestActions[0])
                    elif actionstocurr:
                        bestaction = actionstocurr[0]
                    else:
                        continue
                        print(bestaction)
                    return bestaction



                elif succ_state.isWin():
                    return succ_action[0]
                #if it is neither win nor lose just add to stack
                succ_depth = len(succ_action)
                succ_score = admissibleHeuristic(succ_state) + succ_depth
                fringe.append([succ_depth, succ_state, succ_action, succ_score])
                fringe.sort(key=lambda x: (-x[3]))
