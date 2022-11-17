import random
from typing import List, Tuple


def get_greatest_common_divisor(a: int, b: int) -> int:
    if (a < 0) or (b < 0):
        raise ValueError("Both a and b should be positive integers")
    if b == 0:
        return a
    else:
        return get_greatest_common_divisor(b, a % b)


def get_pairs_of_positive_integers(no_of_pairs: int) -> List[Tuple[int, int]]:
    random.seed(None)
    return list(
        zip(
            random.choices(population=range(1, 21), k=no_of_pairs),
            random.choices(population=range(1, 21), k=no_of_pairs),
        )
    )


def main() -> None:
    print("Greatest Common Divisor (GCD) calculated using Euclid's formula.")
    print("Examples:\n")
    for (a, b) in get_pairs_of_positive_integers(8):
        print(
            "GCD of {0} and {1} = {2}".format(a, b, get_greatest_common_divisor(a, b))
        )
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
