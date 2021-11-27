import numpy as np


def rightPad(inputStr: str, finalLen: int, pad: str) -> str:
    result: str = str(inputStr)
    if result == "16":
        result = "  "
    while len(result) < finalLen:
        result += pad
    return result


class Board(object):
    """
    GameBoard for 15 puzzle game (16 fields, cause 1 is empty)
    """

    def __init__(self) -> None:
        self.__board = np.reshape(np.arange(1, 17), (4, 4))

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
            result += rowStr + "\n" + rowSep + "\n"
        return result


x: Board = Board()
