from typing import List


def getPropDivs(num: int) -> List[int]:
    if num < 0:
        raise ValueError("Cannot compute proper divisors for values below 0")
    elif num == 0:
        return []
    else:
        return [i for i in range(1, num) if num % i == 0]


def getSumOfPropDivs(num1: int) -> int:
    return sum(getPropDivs(num1))


def areAmicablePair(num1: int, num2: int) -> bool:
    return (
        (num1 != num2)
        and (getSumOfPropDivs(num1) == num2)
        and ((getSumOfPropDivs(num2) == num1))
    )


def areListsEql(arr1: List[int], arr2: List[int]) -> bool:
    if len(arr1) != len(arr2):
        return False
    else:
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
    return True


def isSubList(arr1d: List[int], arr2d: List[List[int]]) -> bool:
    for subArr in arr2d:
        if areListsEql(arr1d, subArr):
            return True
    return False


def searchForAmicablePairs(upToExcl: int) -> None:
    results: List[List[int]] = []
    for i in range(upToExcl):
        for j in range(upToExcl):
            if areAmicablePair(i, j) and not isSubList(
                sorted([i, j]), results
            ):
                results.append(sorted([i, j]))
                print("Pair found:", sorted([i, j]))


def displInfoAmicablePairs(searchUpToExcl: int) -> None:
    print("Looking for amicable pairs")
    print("testing numbers  up to (excl): ", searchUpToExcl)
    print("PLEASE BE PATIENT THIS MAY TAKE SOME TIME")
    searchForAmicablePairs(searchUpToExcl)


def main():
    print("Welcome in the program calculating proper divisors of numbers")
    print("====")
    displInfoAmicablePairs(2000)
    print("====")
    print("That is all. Goodbye.")


if __name__ == "__main__":
    main()
