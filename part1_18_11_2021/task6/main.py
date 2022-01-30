from typing import List, Dict


def getPropDiv(num: int) -> List[int]:
    if num < 0:
        raise ValueError("Cannot compute proper divisors for values below 0")
    elif num == 0:
        return []
    else:
        return [i for i in range(1, num) if num % i == 0]


def printInfoPropDivInRange(start: int, end: int) -> None:
    print("Proper divisors for numbers from", start, "to", end - 1, "are:")
    for i in range(start, end):
        print(i, ":", getPropDiv(i))


def getNumsOfPropDivForNumsInRange(start: int, end: int) -> Dict[int, int]:
    result: Dict[int, int] = dict()
    for i in range(start, end):
        result[i] = len(getPropDiv(i))
    return result


def getKeyWithMaxOfDict(numsAndNoOfPropDivs: Dict[int, int]) -> int:
    v: List[int] = list(numsAndNoOfPropDivs.values())
    k: List[int] = list(numsAndNoOfPropDivs.keys())
    return k[v.index(max(v))]


def printInfOfNumWithMaxPropDivInRange(start: int, end: int) -> None:
    print(
        "Calculating proper divisors for numbers from", start, "to", end - 1
    )
    print("Please be patient this may take some time")
    divisors: Dict[int, int] = getNumsOfPropDivForNumsInRange(start, end)
    print("Looking for the number with greatest count of proper divisors")
    print("Please be patient this may also take some time")
    keyOfMax: int = getKeyWithMaxOfDict(divisors)
    print(
        keyOfMax,
        "got",
        divisors[keyOfMax],
        "proper divisors (the most of all the tested numbers)",
    )


def main():
    print("Welcome in the program calculating proper divisors of numbers")
    print("\nRoutine 1")
    printInfoPropDivInRange(1, 11)
    print("\nRoutine 2")
    printInfOfNumWithMaxPropDivInRange(1, 20001)
    print("\nThat is all. Goodbye.")


if __name__ == "__main__":
    main()