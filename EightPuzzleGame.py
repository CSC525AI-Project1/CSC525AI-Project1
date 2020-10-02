'''
Solving Eight Puzzle Game using Search Strategies
The eight-puzzle game is a 3 × 3 version of the 15-puzzle in which eight tiles can be moved around in nine spaces.
CSC 425 525 Artificial Intelligence
Instructor: Dr. Junxiu Zhou
Semester: Fall 2020
Your name:
'''
import numpy as np
import time
from EightPuzzleGame_State import State
from EightPuzzleGame_UninformedSearch import UninformedSearchSolver
from EightPuzzleGame_InformedSearch import InformedSearchSolver


class EightPuzzleGame:
    titles = 8
    def __init__(self, initial=[], goal=[], tiles=8):
        self.initial = initial
        self.goal = goal
        self.tiles = tiles

    def start(self):
        # initialize the init state and goal state as 2d array
        init_tile = np.array([[2, 3, 6], [1, 4, 8], [7, 5, 0]])
        #init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        #init_tile = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]]) #start state added along with additional goal state and h3 prints to test h3


        init = State(init_tile, 0, 0)

        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        #goal_tile = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]) #goal state added along with additional start state and h3 prints to test h3
        goal = State(goal_tile, 0, 0)

        self.tiles = 8
        #t0 = time.time() #start time uninformed solver
        UIS_solver = UninformedSearchSolver(init, goal)
        UIS_solver.run()
        #t1 = time.time()  #end time
        #print("Uninformed search took ", t1-t0, " seconds")
        #t0 = time.time() #start time informed solver
        IS_solver = InformedSearchSolver(init, goal)
        IS_solver.run()
        #t1 = time.time() #end time informed solver
        #print("Uninformed search took ", t1-t0, " seconds")


# start the puzzle game
epp = EightPuzzleGame()
epp.start()