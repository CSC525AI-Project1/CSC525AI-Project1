import numpy as np
from EightPuzzleGame_State import State
import copy

'''
This class implement one of the Uinformed Search algorithm
You may choose to implement the Breadth-first or Depth-first or Iterative-Deepening search algorithm
'''


class UninformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def check_inclusive(self, s):
        """#TODO your code start here"""
        """code for checking if the current state s is already a visited state
        in the list of closed states"""

        """a boolean for determining if a state is already visited, default to false"""
        sameState = False

        """For loop that checks every state in the closed list against the state passed
        by the swap function, if they are the same sets a tracker book to true and does nothing
        if the passed state s is not found in closed"""
        for states in self.closed:
            if (states.tile_seq == s.tile_seq).all() == True:
                sameState = True

        """For loop that checkes every state in the open list to see if the passed state is already
        in the open state, if it is, do not add it again"""
        for states in self.closed:
            if (states.tile_seq == s.tile_seq).all() == True:
                sameState = True

        """if the current state s is not found in the open or closed list, add it to the
         open list to progress the search"""
        if sameState == False:
            tempMatrixOpen = copy.deepcopy(s)
            """Increment the Depth"""
            tempMatrixOpen.depth += 1

            self.openlist.append(tempMatrixOpen)

    # TODO your code end here

    """
    * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """

    def state_walk(self):
        """#TODO your code start here"""

        """create variables for the x and y coordinates of the 0 character"""
        zeroLocationXCord = 0
        zeroLocationYCord = 0

        """find the position of the 0 character
        iterate through the multidimensional array until you find the 0 char
        then set zeroLocationX and Y coordinates variables"""

        for x in range(len(self.current.tile_seq)):
            for y in range(len(self.current.tile_seq[x])):
                if self.current.tile_seq[x, y] == 0:
                    zeroLocationXCord = x
                    zeroLocationYCord = y

        """if statements checking for each valid directional walk and performing
        the swap if it is a valid walk"""

        """if x cord is greater than 0, you can perform an up swap"""
        if zeroLocationXCord > 0:
            """create a temp matrix to overwrite when performing the swap"""
            tempMatrix = copy.deepcopy(self.current)
            """Create a variable to hold the number of the position where zero is moving to"""
            temp = tempMatrix.tile_seq[zeroLocationXCord - 1][zeroLocationYCord]
            """set the number at that position to zero"""
            tempMatrix.tile_seq[zeroLocationXCord - 1][zeroLocationYCord] = 0
            """replace the 0 in the old position with the temp number, completing the swap"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord] = temp
            """check if the new state is already in the visited states closed list"""
            self.check_inclusive(tempMatrix)

        """if y cord is less than 3, you can perform a down swap"""
        if zeroLocationXCord < 2:
            """create a temp matrix to overwrite when performing the swap"""
            tempMatrix = copy.deepcopy(self.current)
            """Create a variable to hold the number of the position where zero is moving to"""
            temp = tempMatrix.tile_seq[zeroLocationXCord + 1][zeroLocationYCord]
            """set the number at that position to zero"""
            tempMatrix.tile_seq[zeroLocationXCord + 1][zeroLocationYCord] = 0
            """replace the 0 in the old position with the temp number, completing the swap"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord] = temp
            self.check_inclusive(tempMatrix)

        """if Y cord is less than 2, you can perform a right swap"""
        if zeroLocationYCord < 2:
            """create a temp matrix to overwrite when performing the swap"""
            tempMatrix = copy.deepcopy(self.current)
            """Create a variable to hold the number of the position where zero is moving to"""
            temp = tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord + 1]
            """set the number at that position to zero"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord + 1] = 0
            """replace the 0 in the old position with the temp number, completing the swap"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord] = temp
            self.check_inclusive(tempMatrix)

        """if Y cord is greater than 0, you can perform a right swap"""
        if zeroLocationYCord > 0:
            """create a temp matrix to overwrite when performing the swap"""
            tempMatrix = copy.deepcopy(self.current)
            """Create a variable to hold the number of the position where zero is moving to"""
            temp = tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord - 1]
            """set the number at that position to zero"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord - 1] = 0
            """replace the 0 in the old position with the temp number, completing the swap"""
            tempMatrix.tile_seq[zeroLocationXCord][zeroLocationYCord] = temp
            self.check_inclusive(tempMatrix)

        """Push the current state to the closed list"""
        self.closed.append(copy.deepcopy(self.current))
        """Pop the front of the list to continue"""
        self.current = self.openlist.pop(0)

    # TODO your code end here

    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            #print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")