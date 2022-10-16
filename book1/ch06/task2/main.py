# -*- coding: utf-8 -*-

import math
import random
from typing import Dict, List, Tuple

nums_to_words: Dict[int, str] = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundered",
}


def get_hundreds(number: int) -> Tuple[int, int]:
    return (100, math.floor(number / 100))


def get_hundreds_str(number: int, mapping: Dict[int, str] = nums_to_words) -> str:
    hundreds: Tuple[int, int] = get_hundreds(number)
    if hundreds[1] == 0:
        return ""
    else:
        return "{0} {1}".format(mapping[hundreds[1]], mapping[hundreds[0]])


def get_tens(number: int) -> Tuple[int, int]:
    tens: int = number % 100
    if tens > 10 and tens < 20:
        return (tens, 1)
    else:
        return (10, math.floor(tens / 10))


def get_tens_str(number: int, mapping: Dict[int, str] = nums_to_words) -> str:
    tens: Tuple[int, int] = get_tens(number)
    tens_single_num: int = tens[0] * tens[1]
    if tens_single_num == 0:
        return ""
    else:
        return mapping[tens_single_num]


def get_ones(number: int) -> Tuple[int, int]:
    tens: int = number % 100
    ones: int = tens % 10
    if tens >= 10 and tens <= 19:
        return (1, 0)
    else:
        return (ones, 1)


def get_ones_str(number: int, mapping: Dict[int, str] = nums_to_words) -> str:
    ones: Tuple[int, int] = get_ones(number)
    ones_single_num: int = ones[0] * ones[1]
    if number == 0:
        return mapping[number]
    elif ones_single_num == 0:
        return ""
    else:
        return mapping[ones_single_num]


def get_number_str(number: int) -> str:
    if (number < 0) or (number > 999):
        raise ValueError("Number must be in range 0-999")
    else:
        return "{0} {1} {2}".format(
            get_hundreds_str(number),
            get_tens_str(number),
            get_ones_str(number),
        ).strip()


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It writes out numbers in the range 0-999 to English.")
    print("The results are print on the screen.")
    print("The numbers are chosen at random.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    random.seed(None)
    examples: List[int] = sorted(random.sample(population=range(0, 1000), k=10))
    for example in examples:
        print("{0}: {1}".format(example, get_number_str(example)))
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
