# -*- coding: utf-8 -*-

import re

# binary, e.g. "0110110"
def get_decimal_from_binary(binary: str) -> int:
    decimal: int = 0
    for i in range(len(binary)):
        decimal += 2 ** i if binary[len(binary) - 1 - i] == "1" else 0
    return decimal


def leave_0s_and_1s(maybe_valid_binary: str) -> str:
    return "".join(list(filter(lambda c: c in ["0", "1"], maybe_valid_binary)))


def lpad_binary_with_0s(binary: str, final_length_multiple_of: int = 4) -> str:
    length_difference: int = len(binary) - final_length_multiple_of
    if length_difference <= 0:
        return "0" * abs(length_difference) + binary
    elif len(binary) % final_length_multiple_of == 0:
        return binary
    else:
        num_of_chars_to_add: int = final_length_multiple_of - (
            len(binary) % final_length_multiple_of
        )
        return "0" * num_of_chars_to_add + binary


def get_string_processed_to_binary(maybe_valid_binary: str) -> str:
    return lpad_binary_with_0s(leave_0s_and_1s(maybe_valid_binary))


# len(binary) must be multiple of n_chars
def get_binary_grouped_by_n_chars(binary: str, n_chars: int = 4, sep: str = " ") -> str:
    return sep.join(re.findall("." * n_chars, binary))


def get_binary_from_user() -> str:
    input_str: str = ""
    input_str = input("\nEnter binary, e.g. '1001011' (only 0s and 1s): ")
    return input_str


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user for a binary number.")
    print("Next it converts it to decimal.")
    print("The result of the conversion is print to the screen.")
    print("Symbols other than 0s and 1s are filtered out.")
    print("If no valid character was found in the input it returns 0.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        binary = get_string_processed_to_binary(get_binary_from_user())
        print("Binary: {0} is: ".format(get_binary_grouped_by_n_chars(binary)))
        print("\tDecimal (my function): {0}".format(get_decimal_from_binary(binary)))
        if len(binary) > 0:
            print("\tDecimal (Python's build-in function): {0}".format(int(binary, 2)))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
