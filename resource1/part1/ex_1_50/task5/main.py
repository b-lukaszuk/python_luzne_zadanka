# -*- coding: utf-8 -*-

from typing import List, Tuple


def get_greatest_common_divisor(m: int, n: int) -> int:
    d: int = min(m, n)
    while not (m % d == 0 and n % d == 0):
        d -= 1
    return d


def get_least_common_multiple(a: int, b: int) -> int:
    return int(abs(a * b) / get_greatest_common_divisor(a, b))


def main() -> None:
    numbers_to_test: List[Tuple[int, int]] = [(36, 12), (18, 12), (30, 25)]
    print("\nThis program finds least common multiple of two numbers.")
    print("Still, no guarantee it works correctly.")
    print("Examples:\n")
    for (int_a, int_b) in numbers_to_test:
        print(
            "lcd({0}, {1}) = {2}".format(
                int_a, int_b, get_least_common_multiple(int_a, int_b)
            )
        )
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
