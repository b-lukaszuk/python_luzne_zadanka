# -*- coding: utf-8 -*-

from typing import List
import random


def get_list_of_rand_nums(
    from_incl: int, to_excl: int, how_many_nums: int = 4
) -> List[int]:
    random.seed(a=None)
    return random.choices(population=range(from_incl, to_excl), k=how_many_nums)


# uses recursion, remember to use relatively short list as arg to function
def get_product(ints: List[int]) -> int:
    if len(ints) == 0:
        raise ValueError("Cannot compute product of empty list.")
    if len(ints) == 1:
        return ints[0]
    return ints[0] * get_product(ints[1:])


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It generates a list of random integers.")
    print("Then it returns the product of all the numbers.")
    print("The product is calculated without loop constructs.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    rand_ints: List[int] = get_list_of_rand_nums(1, 7, 4)
    print_program_description()
    print("The random numbers: {0}".format(rand_ints))
    print("The product of all the numbers:", end=" ")
    print("{0}".format(get_product(rand_ints)))
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
