#!/usr/bin/env python3.8
def rightPad(inputStr: str, finalLen: int, pad: str) -> str:
    result: str = str(inputStr)
    if result == "16":  # no 16 is empty field
        result = "  "
    while len(result) < finalLen:
        result += pad
    return result


def isAnyEltOutsideRange(aList: [int], lowIncl: int, upIncl: int) -> bool:
    belowLow: [bool] = [i < lowIncl for i in aList]
    aboveUp: [bool] = [i > upIncl for i in aList]
    result = any(belowLow) or any(aboveUp)
    return result


def filterOutLstsWithEltsOutsideRange(
    aList: [[int]], lowIncl: int, upIncl: int
) -> [[int]]:
    return list(
        filter(lambda l: not isAnyEltOutsideRange(l, lowIncl, upIncl), aList)
    )
