# -*- coding: utf-8 -*-

import math
from typing import List, Tuple, TypedDict


class Frequeny_Map(TypedDict):
    name: str
    hz_min: float
    hz_max: float


# lower limit of radio waves and upper limit of gamma rays are a bit arbitrary
frequency_map: List[Frequeny_Map] = [
    {
        "name": "radio waves",
        "hz_min": 3 * math.pow(10, 3),
        "hz_max": 3 * math.pow(10, 9),
    },
    {
        "name": "microwaves",
        "hz_min": 3 * math.pow(10, 9),
        "hz_max": 3 * math.pow(10, 12),
    },
    {
        "name": "infrared light",
        "hz_min": 3 * math.pow(10, 12),
        "hz_max": 4.3 * math.pow(10, 14),
    },
    {
        "name": "visible light",
        "hz_min": 4.3 * math.pow(10, 14),
        "hz_max": 7.5 * math.pow(10, 14),
    },
    {
        "name": "ultraviolet light",
        "hz_min": 7.5 * math.pow(10, 14),
        "hz_max": 3 * math.pow(10, 17),
    },
    {
        "name": "x-rays",
        "hz_min": 3 * math.pow(10, 17),
        "hz_max": 3 * math.pow(10, 19),
    },
    {
        "name": "gamma rays",
        "hz_min": 3 * math.pow(10, 19),
        "hz_max": 1 * math.pow(10, 28),
    },
]


def is_num_in_range(num: float, minIncl: float, maxExcl: float) -> bool:
    return (num >= minIncl) and (num < maxExcl)


def get_radiation_name(
    frequency: float, radiation_map: List[Frequeny_Map] = frequency_map
) -> str:
    for radiation in radiation_map:
        if is_num_in_range(frequency, radiation["hz_min"], radiation["hz_max"]):
            return radiation["name"]
    return "radiation type not found"


# Tuple[float, float] is (base, power of 10) for the frequency
def get_user_input(
    unit_names: Tuple[str, str] = ("base", "power of 10"),
    default_frequency: Tuple[float, float] = (3, 5),
    min_input: Tuple[float, float] = (0.1, 3),
    max_input: Tuple[float, float] = (9.9, 27),
) -> Tuple[float, float]:
    result: List[float] = list(default_frequency)
    for i in range(len(unit_names)):
        try:
            input_str: str = input(
                "Enter the the radiation frequency ({0}), i.e. float from {1} to {2}): ".format(
                    unit_names[i], min_input[i], max_input[i]
                )
            )
            result[i] = float(input_str)
            if not is_num_in_range(result[i], min_input[i], max_input[i]):
                raise ValueError
        except ValueError:
            print("Invalid input. I default to {0}".format(default_frequency[i]))
            result[i] = default_frequency[i]
    return tuple(result)


def print_program_description() -> None:
    print("\nHi.\n")
    print(
        "This is a program that asks the user for the frequency of a radiation in Hz."
    )
    print("The input is in the form 'base' and 'power of 10'.")
    print(
        "Based on that (base * 10 ^ power of ten) it calculates the radiation frequency in Hz."
    )
    print("Then it returns the name of the radiation.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF CORRECT RESULT. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    (freq_base, freq_pow_of_10) = get_user_input()
    frequency: float = freq_base * math.pow(10, freq_pow_of_10)
    print(
        "\nThe name of the radiation with frequency of {0:,.0f} Hz is: {1}.".format(
            frequency, get_radiation_name(frequency)
        )
    )
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
