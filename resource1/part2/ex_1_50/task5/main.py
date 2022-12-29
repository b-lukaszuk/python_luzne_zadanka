#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import Callable, List, Union


Number = Union[int, float]


def get_change_betw_consec_elts(nums: List[Number],
                                changeFn: Callable) -> List[Number]:
    nums1_to_n: List[Number] = nums[1:]
    return [changeFn(a, b) for (a, b) in zip(nums1_to_n, nums)]


def get_diffs_betw_consec_elts(nums: List[Number]) -> List[Number]:
    return get_change_betw_consec_elts(nums, lambda x, y: x - y)


def get_progression_rates_betw_consec_elts(nums: List[Number]) -> List[Number]:
    # uses division, so no zeros allowed
    if 0 in nums:
        raise ValueError("The list cannot contain 0s.")
    return get_change_betw_consec_elts(nums, lambda x, y: x / y)


def is_arithm_progress(nums: List[Number]) -> bool:
    diffs: List[Number] = get_diffs_betw_consec_elts(nums)
    return all([diffs[0] == dif for dif in diffs])


def is_geom_progress(nums: List[Number]) -> bool:
    rates: List[Number] = get_progression_rates_betw_consec_elts(nums)
    return all([rates[0] == rate for rate in rates])


def print_info_about_type_of_progress(nums: List[Number]) -> None:
    if len(nums) < 3:
        raise ValueError("Nums must contain at least 3 elements.")
    elif is_arithm_progress(nums):
        print(nums, "is a sequence with arithmetic progress.")
    elif is_geom_progress(nums):
        print(nums, "is a sequence with geometric progress.")
    else:
        print(nums, "- cannot determine the type of progress for the sequence.")


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It tests sequences of numbers for type of sequence progress.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def main() -> None:
    tests: List[List[Number]] = [
        [3, 5, 7, 9, 11, 13],
        [2, 6, 18, 54],
        random.choices(population = range(1, 100), k = 3)
    ]
    print_program_description()
    print("Examples:")
    for test in tests:
        print("-" * 3)
        print_info_about_type_of_progress(test)
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
