from typing import List


def getPropDiv(num: int) -> List[int]:
    if num < 0:
        raise ValueError("Cannot compute proper divisors for values below 0")
    elif num == 0:
        return []
    else:
        return [i for i in range(1, num) if num % i == 0]


def main():
    print("Welcome in the program calculating proper divisors of numbers")
    print("\nThat is all. Goodbye.")


if __name__ == "__main__":
    main()
