# -*- coding: utf-8 -*-

from typing import List, TypedDict


class Color_Map(TypedDict):
    name: str
    wavelength_min: int
    wavelength_max: int


color_map: List[Color_Map] = [
    {"name": "violet", "wavelength_min": 380, "wavelength_max": 427},
    {"name": "indigo", "wavelength_min": 427, "wavelength_max": 450},
    {"name": "blue", "wavelength_min": 450, "wavelength_max": 495},
    {"name": "green", "wavelength_min": 495, "wavelength_max": 570},
    {"name": "yellow", "wavelength_min": 570, "wavelength_max": 590},
    {"name": "orange", "wavelength_min": 590, "wavelength_max": 620},
    {"name": "red", "wavelength_min": 620, "wavelength_max": 751},
]


def is_num_in_range(num: float, minIncl: float, maxExcl: float) -> bool:
    return (num >= minIncl) and (num < maxExcl)


def get_color_name(wavelength_nm: int, color_map: List[Color_Map] = color_map) -> str:
    for color in color_map:
        if is_num_in_range(
            wavelength_nm, color["wavelength_min"], color["wavelength_max"]
        ):
            return color["name"]
    return "color not found"


def get_user_input(
    default_wavelength: int = 500, minInput: int = 380, maxInput: int = 751
) -> int:
    try:
        input_str: str = input(
            "Enter the the wavelength (in nm) of visible light (integer from {0} to {1}): ".format(
                minInput, maxInput - 1
            )
        )
        input_wavelength: int = int(input_str)
        if not is_num_in_range(input_wavelength, minInput, maxInput):
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}".format(default_wavelength))
        input_wavelength = default_wavelength
    return input_wavelength


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a program that asks the user the wavelength of visible light.")
    print("Then it returns the color it represents.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF CORRECT RESULT. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:

    print_program_description()
    wavelength = get_user_input()
    print(
        "\nThe wavelength of {0} nm is perceived as {1}.".format(
            wavelength, get_color_name(wavelength)
        )
    )

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
