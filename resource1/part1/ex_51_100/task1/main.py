# -*- coding: utf-8 -*-

from typing import Tuple


def secs_to_full_days_and_rest(secs: int) -> Tuple[int, int]:
    secs_in_day: int = 60 * 60 * 24
    return divmod(secs, secs_in_day)


def secs_to_full_hours_and_rest(secs: int) -> Tuple[int, int]:
    secs_in_hr: int = 60 * 60
    return divmod(secs, secs_in_hr)


def secs_to_full_minutes_and_rest(secs: int) -> Tuple[int, int]:
    secs_in_min: int = 60
    return divmod(secs, secs_in_min)


def print_secs_to_days_hrs_mins_secs(secs: int) -> None:
    days, rest = secs_to_full_days_and_rest(secs)
    hrs, rest = secs_to_full_hours_and_rest(rest)
    mins, rest = secs_to_full_minutes_and_rest(rest)
    print(
        "{0} [secs] = {1} [days], {2} [hours], {3} [minutes], {4} [seconds]".format(
            secs, days, hrs, mins, rest
        )
    )


def get_int_from_user(msg: str, minIncl: int, maxIncl: int) -> int:
    maybe_int: str = ""
    result_int: int = -999
    while True:
        maybe_int = input(msg)
        try:
            result_int = int(maybe_int)
            if minIncl <= result_int <= maxIncl:
                return result_int
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("That was not an integer. Try again.")


def print_program_description() -> None:
    print("\nHi.")
    print("This is a program that converts seconds to days, hrs, mins, secs.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    seconds: int = get_int_from_user(
        "Enter number of seconds (integer, zero to 10 million) and press Enter: ",
        0,
        10000000,
    )
    print_secs_to_days_hrs_mins_secs(seconds)
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
