# -*- coding: utf-8 -*-

import random
from typing import List

red_spaces: List[int] = [
    1,
    3,
    5,
    7,
    9,
    12,
    14,
    16,
    18,
    19,
    21,
    23,
    25,
    27,
    30,
    32,
    34,
    36,
]

# -1 is 00
all_spaces: List[int] = list(range(-1, 37))


def get_roulette_spin(choices: List[int] = all_spaces) -> int:
    random.seed()
    return random.choice(choices)


def is_result_red(result: int, reds: List[int] = red_spaces) -> bool:
    return result in reds


def is_result_even(result: int) -> bool:
    return result % 2 == 0


def is_result_1_to_18(result: int) -> bool:
    return result >= 1 and result <= 18


def get_pay_declarations(result: int) -> List[str]:
    result_str: str = "00" if result == -1 else "0" if result == 0 else str(result)
    declarations: List[str] = [
        "The spin resulted in {0}".format(result_str),
        "Pay {0}".format(result_str),
    ]
    if result > 0:
        declarations.append("Pay Red" if is_result_red(result) else "Pay Black")
        declarations.append("Pay Even" if is_result_even(result) else "Pay Odd")
        declarations.append("Pay 1 to 18" if is_result_1_to_18(result) else "Pay 19-36")
    return declarations


def print_roulette_spin_description(result: int) -> None:
    for declaration in get_pay_declarations(result):
        print(declaration)


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that simulates a spin of rulette.")
    print("Next it displays the result and some of the payoffs.")
    print("NO GUARANTEE OF ITS ACCURACY. Use it only for fun.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    rulette_result = get_roulette_spin()
    print_roulette_spin_description(rulette_result)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
