# -*- coding: utf-8 -*-

from typing import List
import random


def sort_3_ints(num1: int, num2: int, num3: int) -> List[int]:
    lowest: int = min(num1, num2, num3)
    highest: int = max(num1, num2, num3)
    middle: int = num1 + num2 + num3 - lowest - highest
    return [lowest, middle, highest]


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program that sorts 3 numbers (ascending order).")
    print("It does so without using conditional statements or loops.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    print("Examples. Numbers are drawn at random.")
    random.seed(a=None)
    triples: List[List[int]] = [
        random.choices(population=range(0, 100), k=3) for _ in range(5)
    ]
    for triple in triples:
        print("-" * 3)
        print("Sorting: {0}, {1}, {2}".format(*triple))
        print("Result: {0}".format(sort_3_ints(*triple)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
