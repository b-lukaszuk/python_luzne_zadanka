#!/usr/bin/env python3.8
import random
from typing import List, Dict

daysInYear: int = 365
noOfPeopleAtParty: int = 30
noOfIters: int = 10000


def getPeopleAtParty(howMany: int) -> List[int]:
    people: List[int] = random.choices(
        population=range(daysInYear), k=howMany
    )
    return people


def getValCounts(bDays: List[int]) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for bDay in bDays:
        if bDay in result:
            result[bDay] += 1
        else:
            result[bDay] = 1
    return result


def anySameBDays(bDays: List[int]) -> bool:
    valCounts: Dict[int, int] = getValCounts(bDays)
    for key in valCounts:
        if valCounts[key] > 1:
            return True
    return False


def mean(succsAndFails: List[bool]) -> float:
    noOfSuccs: int = sum(succsAndFails)
    return noOfSuccs / len(succsAndFails)


def runNIters(nIter: int) -> List[bool]:
    result: List[bool] = [
        anySameBDays(getPeopleAtParty(noOfPeopleAtParty))
        for _ in range(nIter)
    ]
    return result


def main() -> None:
    print("====")
    print("Calculating probability of success for:")
    print(
        "at least 2 people at a party celebrating their b-days the same day"
    )
    print("number of people at the party: {:d}".format(noOfPeopleAtParty))
    print("number of iterations: {:d}".format(noOfIters))
    print("Please be patient this may take a while")
    print("p =", mean(runNIters(noOfIters)))
    print("====")
    print("That's all. Goodbye.")


# 0.115 secs for 10k iters, 0.879 secs for 100k iters
if __name__ == "__main__":
    main()
