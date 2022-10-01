# -*- coding: utf-8 -*-

import string


hex_chars_ascending: str = string.digits + string.ascii_lowercase[:6]
decimal_chars_ascending: str = string.digits


def hex2int(hex: str, hex_chars: str = hex_chars_ascending) -> int:
    decimal: int = 0
    for i in range(len(hex)):
        decimal += 16 ** i * hex_chars.index(hex[len(hex) - 1 - i])
    return decimal


def int2hex(decimal: int, hex_chars: str = hex_chars_ascending) -> str:
    hex: str = ""
    after_division: int = decimal
    while after_division != 0:
        hex += hex_chars[after_division % 16]
        after_division = after_division // 16
    return hex[::-1]


def is_valid_string(tested_text: str, allowed_chars: str) -> bool:
    return all([a_letter in allowed_chars for a_letter in tested_text])


def get_input_from_user(allowed_chars: str = hex_chars_ascending) -> str:
    input_str: str = ""
    print("\nEnter a number to convert.")
    print(
        "Convertion type {0}.".format(
            "hex -> decimal" if "f" in allowed_chars else "decimal -> hex"
        )
    )
    print("Allowed chars: {0}".format(allowed_chars))
    input_str = input("Your input (press Enter when you finish): ")
    return input_str


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to enter a number.")
    print("If a number is decimal it converts it to hex.")
    print("If a number is hex it converts it to decimal.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    convert_to_hex: bool = True
    while not end_program:
        print(
            "\nEnter 'h' if you want to convert hex -> decimal, 'd' or anything else will signify conversion decimal -> hex"
        )
        convert_to_hex = input("Your choice [h/d]: ") in ["h", "H"]
        str_to_convert = get_input_from_user(
            hex_chars_ascending if convert_to_hex else decimal_chars_ascending
        ).lower()
        valid_input = is_valid_string(
            str_to_convert,
            hex_chars_ascending if convert_to_hex else decimal_chars_ascending,
        )
        if not valid_input:
            print("Input not valid. No convertion to perform.")
        else:
            print(
                "{0} ({1}) is {2} ({3})".format(
                    "0x" + str_to_convert if convert_to_hex else str_to_convert,
                    "hex" if convert_to_hex else "decimal",
                    hex2int(str_to_convert)
                    if convert_to_hex
                    else "0x" + int2hex(int(str_to_convert)),
                    "decimal" if convert_to_hex else "hex",
                )
            )
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
