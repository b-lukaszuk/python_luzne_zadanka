#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


def throw_error_if_not_positive_integers(num1: int, num2: int) -> None:
    msg: str = "Both num1 and num2 need to be integers greater than 0"
    if not (0 <= num1 and 0 <= num2):
        raise ValueError(msg)
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise ValueError(msg)


def add_2_uints(num1: int, num2: int) -> int:
    throw_error_if_not_positive_integers(num1, num2)
    shift_bits: int = (num1 & num2) << 1
    result: int = num1 ^ num2
    while shift_bits != 0:
        tmp = (result & shift_bits) << 1
        result = result ^ shift_bits
        shift_bits = tmp
    return result


def print_program_info() -> None:
    print("Hi this is a toy program.")
    print("It adds two random unsigned integers without using + sign.")
    print("It does so by using bitwise operations.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press any key (and then Enter) to proceed.")
    print()


def main() -> None:
    print_program_info()
    for _ in range(5):
        random.seed(a = None)
        num1, num2 = (random.randint(0, 200) for _ in range(2))
        print("-" * 3)
        print("Testing addition on 2 numbers: {0} and {1}".format(num1, num2))
        print("Result (bitwise): {0}".format(add_2_uints(num1, num2)))
        print("Result (build-in + function): {0}".format(num1 + num2))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
