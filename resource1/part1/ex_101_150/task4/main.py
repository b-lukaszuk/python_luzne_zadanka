# -*- coding: utf-8 -*-

from typing import List


def are_all_chars_legal(tested_string: str, legal_chars: str = "0123456789.") -> bool:
    return all([ch in legal_chars for ch in tested_string])


def is_num_in_range(num: int, min_incl: int = 0, max_incl: int = 255) -> bool:
    return min_incl <= num <= max_incl


def got_leading_0(num_str: str) -> bool:
    return len(num_str) > 1 and num_str[0] == "0"


def is_num_str_valid(num_str: str) -> bool:
    num: int = 0
    try:
        num = int(num_str)
    except ValueError:
        return False
    return is_num_in_range(num) and not got_leading_0(num_str)


def is_ipv4_legal(ipv4: str) -> bool:
    parts: List[str] = ipv4.split(".")
    if len(parts) != 4:
        return False
    if not are_all_chars_legal(ipv4):
        return False
    for num_str in parts:
        if not is_num_str_valid(num_str):
            return False
    return True


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It tests the corectness of IPv4 addresses.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    print("Testing exemplary addresses (1-3: are OK, 4-8: are NOT OK).")
    maybe_ipv4s: List[str] = [
        "192.168.1.1",
        "192.168.1.0",
        "192.0.2.146",
        "192.168.01.1",
        "192.168.1.00",
        "192.168@1.1",
        "192.0. 2.146",
        "192.0.2.146.3",
    ]
    for maybe_ipv4 in maybe_ipv4s:
        print("-" * 3)
        print("Testing '{0}'".format(maybe_ipv4))
        print("Is correct IPv4? {0}".format(is_ipv4_legal(maybe_ipv4)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
