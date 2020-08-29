import numpy as np
from EightPuzzleGame_State import State

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

    """a boolen for determining if a state is already visited, default to true"""
    sameState = true

    """Code to iterate through every element in the closed list"""
    for states in range(len(closed)):
        """code to iterate through the x values of the current element in the closed list"""
        for x in range(len(closed[states])):
            """code ot iterate through the y values of the current element in the closed list"""
            for y in range(len(closed[x])):
                """if the current element in the x y position of closed is NOT equal to the
                value in the same x y position in the passed state s then the two are different,
                and state s is not currently in the closed list, and should be added"""
                if closed.current[x][y] != s[x][y]:
                    sameState = false

    """if the current state s is not found in the closed list, add it to the closed list"""
    if sameState == false:
        closed.push(s)



       
       
       
    #TODO your code end here

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
    for x in range(len(current)):
        for y in range(len(current[x])):
            if self.current[x][y] == 0:
                zeroLocationXCord = x
                zeroLocationYCord = y

    """if statements checking for each valid directional walk and performing
    the swap if it is a valid walk"""

    """if x cord is greater than 0, you can perform a left swap"""
    if zeroLocationXCord > 0:
        """create a temp matrix to overwrite when performing the swap"""
        tempMatrix = current
        """Create a variable to hold the number of the position where zero is moving to"""
        temp = tempMatrix[zeroLocationXCord-1][zeroLocationYCord]
        """set the number at that position to zero"""
        tempMatrix[zeroLocationXCord-1][zeroLocationYCord] = 0
        """replace the 0 in the old position with the temp number, completing the swap"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord] = temp

        """check if the new state is already in the visited states closed list"""
        checkInclusive(tempMatrix)

    """if x cord is less than 3, you can perform a right swap"""
    if zeroLocationXCord < 3:
        """create a temp matrix to overwrite when performing the swap"""
        tempMatrix = current
        """Create a variable to hold the number of the position where zero is moving to"""
        temp = tempMatrix[zeroLocationXCord + 1][zeroLocationYCord]
        """set the number at that position to zero"""
        tempMatrix[zeroLocationXCord + 1][zeroLocationYCord] = 0
        """replace the 0 in the old position with the temp number, completing the swap"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord] = temp

        """check if the new state is already in the visited states closed list"""
        checkInclusive(tempMatrix)

    """if y cord is greater than 0, you can perform an up swap"""
    if zeroLocationYCord > 0:
        """create a temp matrix to overwrite when performing the swap"""
        tempMatrix = current
        """Create a variable to hold the number of the position where zero is moving to"""
        temp = tempMatrix[zeroLocationXCord][zeroLocationYCord-1]
        """set the number at that position to zero"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord-1] = 0
        """replace the 0 in the old position with the temp number, completing the swap"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord] = temp

        """check if the new state is already in the visited states closed list"""
        checkInclusive(tempMatrix)

    """if y cord is less than 3, you can perform an up swap"""
    if zeroLocationYCord < 3:
        """create a temp matrix to overwrite when performing the swap"""
        tempMatrix = current
        """Create a variable to hold the number of the position where zero is moving to"""
        temp = tempMatrix[zeroLocationXCord][zeroLocationYCord + 1]
        """set the number at that position to zero"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord + 1] = 0
        """replace the 0 in the old position with the temp number, completing the swap"""
        tempMatrix[zeroLocationXCord][zeroLocationYCord] = temp

        """check if the new state is already in the visited states closed list"""
        checkInclusive(tempMatrix)





       
       
       
    #TODO your code end here




    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
