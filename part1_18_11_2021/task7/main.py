from typing import List


def getPropDivs(num: int) -> List[int]:
    if num < 0:
        raise ValueError("Cannot compute proper divisors for values below 0")
    elif num == 0:
        return []
    else:
        return [i for i in range(1, num) if num % i == 0]


def getSumPropDivs(num1: int) -> int:
    return sum(getPropDivs(num1))


def areAmicablePair(num1: int, num2: int) -> bool:
    return (
        (num1 != num2)
        and (getSumPropDivs(num1) == num2)
        and ((getSumPropDivs(num2) == num1))
    )


def main():
    print("Welcome in the program calculating proper divisors of numbers")
    print("\nThat is all. Goodbye.")


if __name__ == "__main__":
    main()
