# -*- coding: utf-8 -*-

from typing import List


def get_7_bits_from_user(default_bit_on_error: int = 1) -> List[int]:
    current_input: str = ""
    bits: List[int] = []
    for i in range(1, 8):
        if i == 1:
            print()
        current_input = input("Enter bit (0 or 1) no. {0}: ".format(i))
        if current_input.strip() not in ["0", "1"]:
            print("Incorrect input, I default to {0}".format(default_bit_on_error))
            bits.append(default_bit_on_error)
        else:
            bits.append(int(current_input))
    return bits


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_count_of_1_bits(bits: List[int]) -> int:
    return sum(bits, 0)


def get_even_parity_bit(bits: List[int]) -> int:
    number_of_1s: int = get_count_of_1_bits(bits)
    return 0 if is_even(number_of_1s) else 1


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that asks the user to enter 7 bits.")
    print("Then it calculates even parity bit (8th bit).")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    bits: List[int] = []
    print_program_description()
    while not end_program:
        bits = get_7_bits_from_user()
        print("The parity bit for: {0} is {1}".format(bits, get_even_parity_bit(bits)))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
