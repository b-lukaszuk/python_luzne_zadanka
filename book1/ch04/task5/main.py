# -*- coding: utf-8 -*-

import re
from typing import List


def is_valid_string(tested_text: str, allowed_chars: str) -> bool:
    return all([a_letter in allowed_chars for a_letter in tested_text])


def is_base_valid(base: str) -> bool:
    valid_chars: bool = is_valid_string(base, "0123456789")
    if valid_chars:
        return 2 <= int(base) <= 16
    else:
        return False


def is_input_ok(
    base_n_number: str, base: int, available_chars: str = "0123456789abcdef"
) -> bool:
    if not is_valid_string(base_n_number, available_chars[:base]):
        return False
    else:
        return True


def are_inputs_ok(
    num_to_convert: str, base_convert_from: str, base_convert_to: str
) -> bool:
    return (
        is_base_valid(base_convert_from)
        and is_base_valid(base_convert_to)
        and is_input_ok(num_to_convert, int(base_convert_from))
    )


def base_n_to_decimal(
    base_n_number: str, base: int, available_chars: str = "0123456789abcdef"
) -> int:
    chars_to_use: str = available_chars[:base]
    decimal: int = 0
    input_length: int = len(base_n_number)
    for i in range(input_length):
        decimal += base ** i * chars_to_use.index(base_n_number[input_length - 1 - i])
    return decimal


def decimal_to_base_n(
    decimal: str, base_n: int, available_chars: str = "0123456789abcdef"
) -> str:
    base_n_number: str = ""
    after_division: int = int(decimal)
    while after_division != 0:
        base_n_number += available_chars[after_division % base_n]
        after_division = after_division // base_n
    return base_n_number[::-1]


def convert_num_base_n_to_num_base_m(
    number_base_n: str, base_n: int, base_m: int
) -> str:
    if base_n == base_m:
        return number_base_n
    else:
        decimal: int = base_n_to_decimal(number_base_n, base_n)
        return decimal_to_base_n(str(decimal), base_m)


def pad_num_base_n_with_spaces(
    num_base_n: str, final_length_multiple_of: int = 4
) -> str:
    length_difference: int = len(num_base_n) - final_length_multiple_of
    if length_difference <= 0:
        return " " * abs(length_difference) + num_base_n
    else:
        return " " * (len(num_base_n) % final_length_multiple_of) + num_base_n


def get_num_base_n_grouped_by_m_chars(number_base_n: str, m_chars: int = 4) -> str:
    return " ".join(re.findall("." * m_chars, number_base_n))


def format_number_base_n(number_base_n: str) -> str:
    return get_num_base_n_grouped_by_m_chars(
        pad_num_base_n_with_spaces(number_base_n)
    ).lstrip()


def get_input_from_user() -> List[str]:
    names_of_inputs: List[str] = [
        "number to convert",
        "base of the number to convert from",
        "base of the number to convert to",
    ]
    inputs: List[str] = ["", "", ""]
    for i in range(len(names_of_inputs)):
        if i == 0:
            print()
        inputs[i] = input(
            "Enter {0} and press Enter: ".format(names_of_inputs[i])
        ).lower()
    return inputs


def declare_conversion(
    num_to_convert: str, base_convert_from: str, base_convert_to: str
) -> None:
    print(
        "'{0}' (base {1}) = '{2}' (base {3})".format(
            format_number_base_n(num_to_convert),
            base_convert_from,
            format_number_base_n(
                convert_num_base_n_to_num_base_m(
                    num_to_convert, int(base_convert_from), int(base_convert_to)
                )
            ),
            base_convert_to,
        )
    )


def declare_inputs_validity(
    num_to_convert: str, base_convert_from: str, base_convert_to: str
) -> None:
    if not is_base_valid(base_convert_from):
        print("Base 'to convert from' is invalid. No conversion done.")
    if not is_base_valid(base_convert_to):
        print("Base 'to convert to' is invalid. No conversion done.")
    if not is_input_ok(num_to_convert, int(base_convert_from)):
        print(
            "The input: '{0}' contains characters not in: '{1}'. No conversion done.".format(
                num_to_convert, "0123456789abcdef"[: int(base_convert_from)]
            )
        )


def validate_inputs_and_declare_conversion(
    num_to_convert: str, base_convert_from: str, base_convert_to: str
) -> None:
    print("Validating inputs.")
    if not are_inputs_ok(num_to_convert, base_convert_from, base_convert_to):
        print("Validation failed.")
        declare_inputs_validity(num_to_convert, base_convert_from, base_convert_to)
    else:
        print("Inputs are valid. Proceeding with conversion.")
        declare_conversion(num_to_convert, base_convert_from, base_convert_to)


def handle_user_input() -> None:
    validate_inputs_and_declare_conversion(*get_input_from_user())


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to enter a number.")
    print("Then the user specifies the base of this number (2 to 16).")
    print(
        "Next, the user is asked to what base (2-16) should the number be converted to."
    )
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        handle_user_input()
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
