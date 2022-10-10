# -*- coding: utf-8 -*-

import random
from typing import List, Union

# Union type declaration
Number = Union[int, float]


def countRange(numbers: List[Number], min: Number, max: Number) -> int:
    return len([number for number in numbers if (min <= number <= max)])


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that creates a few random lists.")
    print("Then it determines how many elements of a list are within a certain range.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def declare_result_of_simulation(min: Number = 20, max: Number = 40) -> None:
    nums: List[Number] = random.choices(population=range(100), k=10)
    print(
        "List {0} number of elements between {1} (inclusive) and {2} (inclusive) = {3}".format(
            nums, min, max, countRange(nums, 20, 40)
        )
    )


def main() -> None:
    print_program_description()
    for _ in range(3):
        declare_result_of_simulation()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
