from typing import List


def getPropDivs(num: int) -> List[int]:
    if num <= 0:
        raise ValueError("Cannot compute proper divisors for values <= 0")
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


def searchForAmicablePairs(upToExcl: int) -> None:
    for i in range(1, upToExcl):
        for j in range(i, upToExcl):
            if areAmicablePair(i, j):
                print("Pair found:", [i, j])


def displInfoAmicablePairs(searchUpToExcl: int) -> None:
    print("Looking for amicable pairs")
    print("testing numbers  up to (excl): ", searchUpToExcl)
    print("PLEASE BE PATIENT THIS MAY TAKE SOME TIME")
    searchForAmicablePairs(searchUpToExcl)


def main() -> None:
    print("Welcome in the program calculating proper divisors of numbers")
    print("====")
    displInfoAmicablePairs(2000)
    print("====")
    print("That is all. Goodbye.")


if __name__ == "__main__":
    main()
