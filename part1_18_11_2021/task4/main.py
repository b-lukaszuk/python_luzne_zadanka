import numpy as np
from typing import List

# based on:
# https://www.youtube.com/watch?v=GuCzYxHa7iA
# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# and my own invention

goalBoard: np.ndarray = np.reshape(np.arange(1, 17), (4, 4))

initialBoard: np.ndarray = np.reshape(
    [10, 8, 12, 9, 13, 4, 7, 2, 5, 3, 6, 16, 1, 11, 14, 15], (4, 4)
)

emptyField: int = 16


def isAnyEltOutsideRange(aList: List[int], lowIncl: int, upIncl: int) -> bool:
    belowLow: List[bool] = [i < lowIncl for i in aList]
    aboveUp: List[bool] = [i > upIncl for i in aList]
    result = any(belowLow) or any(aboveUp)
    return result


def removeEltsOutsideRange(
    aList: List[List[int]], lowIncl: int, upIncl: int
) -> List[List[int]]:
    return list(
        filter(lambda l: not isAnyEltOutsideRange(l, lowIncl, upIncl), aList)
    )


def getLoc(numToFind: int, board: np.ndarray) -> List[int]:
    theLoc: np.ndarray = np.where(board == numToFind)
    return [theLoc[0][0], theLoc[1][0]]


def getLegMovesLocs(arr2d: np.ndarray) -> List[List[int]]:
    emptyLoc: List[int] = getLoc(emptyField, arr2d)
    neighLocs: List[List[int]] = []
    nrow, ncol = emptyLoc
    neighLocs.extend([[nrow, ncol - 1], [nrow, ncol + 1]])
    neighLocs.extend([[nrow - 1, ncol], [nrow + 1, ncol]])
    neighLocs = removeEltsOutsideRange(neighLocs, 0, arr2d.shape[0] - 1)
    return neighLocs


def getLegMoves(arr2d: np.ndarray) -> List[int]:
    neighLocs: List[List[int]] = getLegMovesLocs(arr2d)
    return [arr2d[r, c] for [r, c] in neighLocs]


def getManhDistance(
    noOfInterest: int, curBoard: np.ndarray, solvedBoard: np.ndarray
) -> int:
    if noOfInterest == emptyField:
        return 0
    else:
        cRow, cCol = getLoc(noOfInterest, curBoard)
        sRow, sCol = getLoc(noOfInterest, solvedBoard)
        return abs(cRow - sRow) + abs(cCol - sCol)


def getLen(arr2d: np.ndarray) -> int:
    dims: List[int] = arr2d.shape
    return dims[0] * dims[1]


# G cost - number of steps taken from initState to curState
# H cost - number of steps taken from curState to goalState
def calcCost(state1: np.ndarray, state2: np.ndarray) -> int:
    costs: List[int] = [0] * getLen(state1)
    for r in range(state1.shape[0]):
        for c in range(state1.shape[1]):
            costs[(r * c) + c] = getManhDistance(state1[r, c], state1, state2)
    return sum(costs)


def getHCost(curState: np.ndarray) -> int:
    return calcCost(curState, goalBoard)


def getGCost(curState: np.ndarray) -> int:
    return calcCost(curState, initialBoard)


# F cost = G cost + H cost
def getFCost(curState: np.ndarray) -> int:
    hCost: int = getHCost(curState)
    gCost: int = getGCost(curState)
    return hCost + gCost


def mkMove(numToMove: int, arr2d: np.ndarray) -> np.ndarray:
    if (numToMove != emptyField) and (numToMove in getLegMoves(arr2d)):
        numR, numC = getLoc(numToMove, arr2d)
        emptyR, emptyC = getLoc(emptyField, arr2d)
        arr2dCopy: np.ndarray = np.copy(arr2d)
        arr2dCopy[numR, numC] = emptyField
        arr2dCopy[emptyR, emptyC] = numToMove
        return arr2dCopy
    else:
        raise ValueError("Wrong number. Illegal move.")


def getNextStates(arr2d: np.ndarray) -> List[np.ndarray]:
    legMoves: List[int] = getLegMoves(arr2d)
    return [mkMove(move, arr2d) for move in legMoves]


def isEql(arr2d1: np.ndarray, arr2d2: np.ndarray) -> bool:
    return np.array_equal(arr2d1, arr2d2)


def isInForbiddenStates(
    arr2d: np.ndarray, forbStates: List[np.ndarray]
) -> bool:
    for fState in forbStates:
        if isEql(arr2d, fState):
            continue
        else:
            return False
    return True


def rmForbiddenStates(
    newStates: List[np.ndarray], forbStates: List[np.ndarray]
) -> List[np.ndarray]:
    result: List[np.ndarray] = []
    for newState in newStates:
        if not isInForbiddenStates(newState, forbStates):
            result.append(newState)
    return result
