# -*- coding: utf-8 -*-

from typing import Any, List, TypeVar
import random

T = TypeVar("T")


def get_sublists_of_len_n(some_list: List[T], n) -> List[List[T]]:
    result: List[List[T]] = []
    len_some_list: int = len(some_list)
    start_ind: int = 0
    end_ind: int = n
    if n <= 0 or n > len_some_list:
        raise ValueError("n cannot be <= 0 nor >= length of some_list")
    while end_ind <= len_some_list:
        result.append(some_list[start_ind:end_ind])
        start_ind += 1
        end_ind += 1
    return result


def get_all_sublists(some_list: List[T]) -> List[List[T]]:
    result: List[List[T]] = []
    for i in range(1, len(some_list) + 1):
        result.extend(get_sublists_of_len_n(some_list, i))
    return result


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that returns sublists from a list.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()
    random.seed(None)
    exemplary_lists: List[List[Any]] = [
        [1, 2, 3, 4],
        random.sample(range(10), 5),
        list("Hello"),
    ]
    for a_list in exemplary_lists:
        print("\nA list: {0}".format(a_list))
        print("It's sublists:\n{0}".format(get_all_sublists(a_list)))
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
