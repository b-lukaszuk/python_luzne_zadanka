#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from typing import Callable, List, Tuple


def is_bit(bit1: str) -> bool:
    return bit1 in "01"


def raise_errors_if_not_bits(bit1: str, bit2: str) -> None:
    if not (is_bit(bit1) and is_bit(bit2)):
        raise ValueError("bit must be 0 or 1")


def all_bits_equal_0(bits: str) -> bool:
    return all([ch == "0" for ch in bits])


def get_xor_of_2_bits(bit1: str, bit2: str) -> str:
    raise_errors_if_not_bits(bit1, bit2)
    return "1" if (bit1 != bit2) else "0"


def get_shift_bit(bit1: str, bit2: str) -> str:
    raise_errors_if_not_bits(bit1, bit2)
    return "1" if (bit1 == "1" and bit2 == "1") else "0"


def get_equalized_binary_nums(bin_num1: str, bin_num2: str) -> Tuple[str, str]:
    max_len: int = max(len(bin_num1), len(bin_num2))
    num1 = bin_num1.rjust(max_len, "0")
    num2 = bin_num2.rjust(max_len, "0")
    return (num1, num2)


def apply_bin_fn_on_bit_pairs_of_bin_nums(bin_num1: str, bin_num2: str,
                                          fn: Callable[[str, str], str]) -> str:
    num1, num2 = get_equalized_binary_nums(bin_num1, bin_num2)
    result: List[str] = [fn(a, b) for (a, b) in zip(num1, num2)]
    return "".join(result)


def get_xor_of_2_binary_nums(bin_num1: str, bin_num2: str) -> str:
    return apply_bin_fn_on_bit_pairs_of_bin_nums(
        bin_num1, bin_num2, get_xor_of_2_bits)


def get_shift_bits_of_2_binary_nums(bin_num1: str, bin_num2: str) -> str:
    return apply_bin_fn_on_bit_pairs_of_bin_nums(
        bin_num1, bin_num2, get_shift_bit)


def int2bin(num: int) -> str:
    msg: str = "Only positive integers can be converted to binary."
    if num < 0:
        raise ValueError(msg)
    if not isinstance(num, int):
        raise ValueError(msg)
    return bin(num)[2:]


def add_2_uints(num1: int, num2: int) -> int:
    bin1: str = int2bin(num1)
    bin2: str = int2bin(num2)
    shift_bits: str = get_shift_bits_of_2_binary_nums(bin1, bin2) + "0"
    result: str = get_xor_of_2_binary_nums(bin1, bin2)
    while not all_bits_equal_0(shift_bits):
        tmp = get_shift_bits_of_2_binary_nums(result, shift_bits) + "0"
        result = get_xor_of_2_binary_nums(result, shift_bits)
        shift_bits = tmp
    return int(result, base=2)


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
