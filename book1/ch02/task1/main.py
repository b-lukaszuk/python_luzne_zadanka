# -*- coding: utf-8 -*-


def isNumBetween(num: float, minIncl: float, maxIncl: float) -> bool:
    return (num >= minIncl) and (num <= maxIncl)


def get_user_input(
    default_on_error: int = 2, minInput: int = 1, maxInput: int = 27
) -> int:
    try:
        input_str: str = input(
            "Enter the age of a dog in human years (integer from {0} to {1}): ".format(
                minInput, maxInput
            )
        )
        dogs_age: int = int(input_str)
        if not isNumBetween(dogs_age, minInput, maxInput):
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}\n".format(default_on_error))
        dogs_age = default_on_error
    return dogs_age


def get_dog_years(human_years: int) -> float:
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a program that asks the user for the age of a dog in human years.")
    print("Then it calculates the age of the dog in dog years.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF CORRECT CONVERSION.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    dog_age_human_years = get_user_input()
    print(
        "{0} human year(s) is {1} dog years".format(
            dog_age_human_years, get_dog_years(dog_age_human_years)
        )
    )

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
