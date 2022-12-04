# -*- coding: utf-8 -*-


def get_float_from_user(msg: str, minIncl: float, maxIncl: float) -> float:
    maybe_float: str = ""
    result_float: float = -999
    while True:
        maybe_float = input(msg)
        try:
            result_float = float(maybe_float)
            if minIncl <= result_float <= maxIncl:
                return result_float
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("That was not a number. Try again.")


def get_bmi(weight_kg: float, height_cm: float) -> float:
    return weight_kg / (height_cm / 100) ** 2


def print_program_description() -> None:
    print("\nHi.")
    print("This is a program that calculates BMI (body mass index)", end=" ")
    print("based on a data entered by user.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    body_mass_kg: float = get_float_from_user(
        "Enter body weight [kg, 1-650] and press Enter: ", 1, 650
    )
    height_cm: float = get_float_from_user(
        "Enter height [cm, 20-280] and press Enter: ", 20, 280
    )
    print(
        "A person {0:.2f} [cm] tall and {1:.2f} [kg] heavy got BMI equal {2:.2f} [kg/m^2]".format(
            height_cm, body_mass_kg, get_bmi(body_mass_kg, height_cm)
        )
    )
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
