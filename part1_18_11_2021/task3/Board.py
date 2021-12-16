#!/usr/bin/env python3.8
import numpy as np
import utils as ut


class Board(object):
    """
    GameBoard for 15 puzzle game (16 fields, cause 1 is empty, i.e. no 16)
    """

    def __init__(self) -> None:
        self.__solution = np.arange(1, 17)
        while True:
            self.__board = np.copy(self.__solution)
            np.random.shuffle(self.__board)
            self.__board = np.reshape(self.__board, (4, 4))
            if self.__isSolvable():
                break

    def __str__(self) -> str:
        fieldLen: int = len(str(self.__board.max())) + 1
        colSep: str = "|"
        rowSepSingleCell: str = "+" + ut.rightPad("-", fieldLen, "-")
        nrow, ncol = self.__board.shape
        rowSep: str = (
            ut.rightPad(
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
                rowStr += ut.rightPad(self.__board[r, c], fieldLen, " ")
                rowStr += colSep
            result += rowStr + "\n" + rowSep
            if r != (nrow - 1):
                result += "\n"
        return result

    def __repr__(self) -> str:
        return self.__str__()

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
        return ut.filterOutLstsWithEltsOutsideRange(
            locsOfNearbyFields, 0, self.__board.shape[0] - 1
        )

    def __swapNumsOnBoard(self, num1: int, num2: int) -> None:
        locNum1r, locNum1c = self.__getLocOfNum(num1)
        locNum2r, locNum2c = self.__getLocOfNum(num2)
        self.__board[locNum1r, locNum1c] = num2
        self.__board[locNum2r, locNum2c] = num1

    def __getLegalMoves(self) -> [int]:
        locsNearEmpty: [[int]] = self.__getLocsOfFieldsNearEmpty()
        result: [int] = [self.__board[r, c] for (r, c) in locsNearEmpty]
        return result

    # from
    # https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    # modified by me

    # in the example blank is equal to 0
    # in my program it is 16 (that's why I got break in for loop with i)
    def __getInversionsCount(self) -> int:
        invCount: int = 0
        nrows: int = self.__board.shape[0]
        arr1d: np.ndarray = self.__board.flatten()
        for i in range(nrows * nrows - 1):
            if arr1d[i] == 16:
                continue
            for j in range(i + 1, nrows * nrows):
                if i < j and arr1d[i] > arr1d[j]:
                    invCount += 1
                    return invCount

    # find Position of blank (16) from bottom
    # number of moves it takes to move from original position (3, 3)
    # to the position it is now
    def __findBlankPos(self) -> int:
        nrows: int = self.__board.shape[0]
        for i in range(nrows - 1, -1, -1):
            for j in range(nrows - 1, -1, -1):
                if self.__board[i, j] == 16:
                    return nrows - i

    def __isSolvable(self) -> bool:
        numberOfInversions: int = self.__getInversionsCount()
        # if grid is odd, return true if inversion count is even
        if ut.isOdd(self.__board.shape[0]) and ut.isEven(numberOfInversions):
            return True
        else:  # grid is Even
            posOfEmpty: int = self.__findBlankPos()
            if ut.isEven(posOfEmpty) and ut.isOdd(numberOfInversions):
                return True
            if ut.isOdd(posOfEmpty) and ut.isEven(numberOfInversions):
                return True
        return False

    def isMoveLegal(self, move: int) -> bool:
        legMoves: [int] = self.__getLegalMoves()
        return move in legMoves

    def makeMove(self, move: int) -> None:
        if self.isMoveLegal(move):
            self.__swapNumsOnBoard(16, move)  # 16 i empty field

    def isBoardSolved(self) -> bool:
        return np.array_equal(self.__board, self.__solution)
