# -*- coding: utf-8 -*-

from typing import List
import random


def get_list_of_rand_nums(
    from_incl: int, to_excl: int, how_many_nums: int = 15
) -> List[int]:
    random.seed(a=None)
    return random.choices(population=range(from_incl, to_excl), k=how_many_nums)


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It takes a list of random integers.")
    print("Then it returns the numbers divisible by 15, using lambda function.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    rand_ints: List[int] = get_list_of_rand_nums(1, 201, 15)
    print_program_description()
    print("The random integers: {0}".format(rand_ints))
    print("The numbers divisible by 15 (empty list if none):", end=" ")
    print("{0}".format(list(filter(lambda x: (x % 15 == 0), rand_ints))))
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
