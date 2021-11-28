import numpy as np


def rightPad(inputStr: str, finalLen: int, pad: str) -> str:
    result: str = str(inputStr)
    if result == "16":  # no 16 is empty field
        result = "  "
    while len(result) < finalLen:
        result += pad
    return result


def isAnyEltOutsideRange(aList: [int], lowIncl: int, upIncl: int) -> bool:
    belowLow: [bool] = [i < lowIncl for i in aList]
    # print(belowLow)
    aboveUp: [bool] = [i > upIncl for i in aList]
    # print(aboveUp)
    # print(any(belowLow))
    # print(any(aboveUp))
    result = any(belowLow) or any(aboveUp)
    return result


def filterOutLstsWithEltsOutsideRange(
    aList: [[int]], lowIncl: int, upIncl: int
) -> [[int]]:
    return list(
        filter(lambda l: not isAnyEltOutsideRange(l, lowIncl, upIncl), aList)
    )


class Board(object):
    """
    GameBoard for 15 puzzle game (16 fields, cause 1 is empty, i.e. no 16)
    """

    def __init__(self) -> None:
        self.__board = np.arange(1, 17)
        self.__solution = np.copy(self.__board)
        np.random.shuffle(self.__board)
        self.__board = np.reshape(self.__board, (4, 4))

    def __str__(self) -> str:
        fieldLen: int = len(str(self.__board.max())) + 1
        colSep: str = "|"
        rowSepSingleCell: str = "+" + rightPad("-", fieldLen, "-")
        nrow, ncol = self.__board.shape
        rowSep: str = (
            rightPad(
                rowSepSingleCell,
                ncol * len(rowSepSingleCell),
                rowSepSingleCell,
            )
            + "+"
        )
        result: str = rowSep + "\n"
        for r in range(nrow):
            rowStr: str = "|"
            for c in range(ncol):
                rowStr += rightPad(self.__board[r, c], fieldLen, " ")
                rowStr += colSep
            result += rowStr + "\n" + rowSep
            if r != (nrow - 1):
                result += "\n"
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def getBoard(self) -> np.ndarray:  # for testing
        return self.__board

    def __getLocOfNum(self, num: int) -> [int, int]:
        result: [np.ndarray, np.ndarray] = np.where(self.__board == num)
        return [result[0][0], result[1][0]]

    def __getLocOfEmpty(self) -> [int, int]:  # no 16 is empty field
        return self.__getLocOfNum(16)

    def __getLocsOfFieldsNearEmpty(self) -> [[int]]:
        locOfEmpty: [int, int] = self.__getLocOfEmpty()
        locsOfNearbyFields: [[int]] = []
        nrow, ncol = locOfEmpty
        locsOfNearbyFields.extend([[nrow, ncol - 1], [nrow, ncol + 1]])
        locsOfNearbyFields.extend([[nrow - 1, ncol], [nrow + 1, ncol]])
        return filterOutLstsWithEltsOutsideRange(
            locsOfNearbyFields, 0, self.__board.shape[0] - 1
        )

    def __moveDown(self, move: int) -> None:
        locEmpty: [int, int] = self.__getLocOfEmpty()
        numsOfRowsAbove: [int] = list(range(0, locEmpty[0]))
        oldRowsNums: [int] = [locEmpty[0]] + numsOfRowsAbove
        newRowsNums: [int] = [numsOfRowsAbove[0]] + [
            i + 1 for i in numsOfRowsAbove
        ]
        newBoard: np.ndarray = np.copy(self.__board)
        for i in range(len(newRowsNums)):
            newBoard[newRowsNums[i], locEmpty[1]] = self.__board[
                oldRowsNums[i], locEmpty[1]
            ]
        self.__board = newBoard

    def __moveUp(self, move: int) -> None:
        locEmpty: [int, int] = self.__getLocOfEmpty()
        numsOfBelow: [int] = list(range(locEmpty[0], self.__board.shape[0]))
        oldRowsNums: [int] = numsOfBelow + [locEmpty[0]]
        newRowsNums: [int] = [i - 1 for i in numsOfBelow] + [numsOfBelow[-1]]
        newBoard: np.ndarray = np.copy(self.__board)
        for i in range(len(newRowsNums)):
            newBoard[newRowsNums[i], locEmpty[1]] = self.__board[
                oldRowsNums[i], locEmpty[1]
            ]
        self.__board = newBoard

    def __moveRight(self, move: int) -> None:
        locEmpty: [int, int] = self.__getLocOfEmpty()
        numsOnLeft: [int] = list(range(0, locEmpty[1]))
        oldColsNums: [int] = [locEmpty[1]] + numsOnLeft
        newColsNums: [int] = [numsOnLeft[0]] + [i + 1 for i in numsOnLeft]
        newBoard: np.ndarray = np.copy(self.__board)
        for i in range(len(newColsNums)):
            newBoard[locEmpty[0], newColsNums[i]] = self.__board[
                locEmpty[0], oldColsNums[i]
            ]
        self.__board = newBoard

    def __moveLeft(self, move: int) -> None:
        locEmpty: [int, int] = self.__getLocOfEmpty()
        numsOnRight: [int] = list(range(locEmpty[1], self.__board.shape[1]))
        oldColsNums: [int] = numsOnRight + [locEmpty[1]]
        newColsNums: [int] = [i - 1 for i in numsOnRight] + [numsOnRight[-1]]
        newBoard: np.ndarray = np.copy(self.__board)
        for i in range(len(newColsNums)):
            newBoard[locEmpty[0], newColsNums[i]] = self.__board[
                locEmpty[0], oldColsNums[i]
            ]
        self.__board = newBoard

    def __getLegalMoves(self) -> [int]:
        locsNearEmpty: [[int]] = self.__getLocsOfFieldsNearEmpty()
        result: [int] = [self.__board[r, c] for (r, c) in locsNearEmpty]
        return result

    def isMoveLegal(self, move: int) -> bool:
        legMoves: [int] = self.__getLegalMoves()
        return move in legMoves

    def makeMove(self, move: int) -> None:
        emptyLoc: [int, int] = self.__getLocOfEmpty()
        moveLoc: [int, int] = self.__getLocOfNum(move)
        if emptyLoc[0] == moveLoc[0] and emptyLoc[1] < moveLoc[1]:
            self.__moveLeft(move)
        elif emptyLoc[0] == moveLoc[0] and emptyLoc[1] > moveLoc[1]:
            self.__moveRight(move)
        elif emptyLoc[0] < moveLoc[0] and emptyLoc[1] == moveLoc[1]:
            self.__moveUp(move)
        else:
            self.__moveDown(move)

    def isBoardSolved(self) -> bool:
        return np.array_equal(self.__board, self.__solution)


x: Board = Board()
