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
    GameBoard for 15 puzzle game (16 fields, cause 1 is empty)
    """

    def __init__(self) -> None:
        self.__board = np.arange(1, 17)
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

    def __getLocOfNum(self, num: int) -> (int, int):
        result: (np.ndarray, np.ndarray) = np.where(self.__board == num)
        return (result[0][0], result[1][0])

    def __getLocOfEmpty(self) -> (int, int):  # no 16 is empty field
        return self.__getLocOfNum(16)

    def __getLocsOfFieldsNearEmpty(self) -> [[int]]:
        locOfEmpty: (int, int) = self.__getLocOfEmpty()
        locsOfNearbyFields: [[int]] = []
        nrow, ncol = locOfEmpty
        locsOfNearbyFields.extend([[nrow, ncol - 1], [nrow, ncol + 1]])
        locsOfNearbyFields.extend([[nrow - 1, ncol], [nrow + 1, ncol]])
        return filterOutLstsWithEltsOutsideRange(
            locsOfNearbyFields, 0, self.__board.shape[0] - 1
        )

    def __getLegalMoves(self) -> [int]:
        locsNearEmpty: [[int]] = self.__getLocsOfFieldsNearEmpty()
        result: [int] = [self.__board[r, c] for (r, c) in locsNearEmpty]
        return result

    def isMoveLegal(self, move: int) -> bool:
        legMoves: [int] = self.__getLegalMoves()
        return move in legMoves


x: Board = Board()
