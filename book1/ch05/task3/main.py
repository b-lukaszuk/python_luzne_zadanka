# -*- coding: utf-8 -*-

from typing import List
import random


def get_6_numbers_fn1(min_incl: int = 1, max_incl: int = 49) -> List[int]:
    random_nums: List[int] = []
    random.seed()
    while len(random_nums) < 6:
        cur_num: int = random.randint(min_incl, max_incl)
        if cur_num not in random_nums:
            random_nums.append(cur_num)
    return sorted(random_nums)


def get_6_numbers_fn2(min_incl: int = 1, max_incl: int = 49) -> List[int]:
    random.seed()
    return sorted(random.sample(range(min_incl, max_incl + 1), 6))


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that imitates lottery results.")
    print("It draws 6 numbers from 1 to 49 without repetition.")
    print("Next it prints the result on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        print("\nThe drawn random lottery numbers (6 numbers from 1 to 49) are:")
        print("\tMethod 1: {0}".format(get_6_numbers_fn1()))
        print("\tMethod 2: {0}".format(get_6_numbers_fn2()))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
