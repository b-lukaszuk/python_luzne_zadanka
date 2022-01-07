import numpy as np

# based on:
# https://www.youtube.com/watch?v=GuCzYxHa7iA
# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# and my own invention

goalBoard: np.ndarray = np.reshape(np.arange(1, 17), (4, 4))

startBoard: np.ndarray = np.reshape(
    [10, 8, 12, 9, 13, 4, 7, 2, 5, 3, 6, 16, 1, 11, 14, 15], (4, 4)
)


def getLoc(numToFind: int, board: np.ndarray) -> [int, int]:
    theLoc: np.ndarray = np.where(board == numToFind)
    return [theLoc[0][0], theLoc[1][0]]


def getManhDistance(
    noOfInterest: int, curBoard: np.ndarray, solvedBoard: np.ndarray
) -> int:
    cLoc: [int, int] = getLoc(noOfInterest, curBoard)
    sLoc: [int, int] = getLoc(noOfInterest, solvedBoard)
    return abs(cLoc[0] - sLoc[0]) + abs(cLoc[1] - sLoc[1])


def getLen(arr2d: np.ndarray) -> int:
    dims: (int, int) = arr2d.shape
    return dims[0] * dims[1]


# G cost - number of steps taken from initState to curState
# H cost - number of steps taken from curState to goalState
def calcCost(state1: np.ndarray, state2: np.ndarray) -> int:
    costs: [int] = [0] * getLen(state1)
    for r in range(state1.shape[0]):
        for c in range(state1.shape[1]):
            costs[(r * c) + c] = getManhDistance(state1[r, c], state1, state2)
    return sum(costs)
