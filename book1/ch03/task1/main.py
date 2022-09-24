# -*- coding: utf-8 -*-

from typing import List


def get_guest_ages_from_user(default_age_on_error: int = 10) -> List[int]:
    current_input: str = ""
    guest_number: int = 1
    results: List[int] = []
    end: bool = False
    while not end:
        current_input = input("Enter age of a guest {0}: ".format(guest_number))
        guest_number += 1
        if current_input.strip() == "":
            print("End of input recognized")
            end = True
        else:
            try:
                results.append(int(current_input))
            except ValueError:
                print("Incorrect input. I default to {0}".format(default_age_on_error))
                results.append(int(default_age_on_error))
    return results


def filter_out_incorrect_ages(guest_ages: List[int]) -> List[int]:
    return list(filter(lambda age: age >= 0 and age <= 125, guest_ages))


def calculate_total_price_usd(guest_ages: List[int]) -> int:
    sum_usd: int = 0
    for age in guest_ages:
        if age < 3:
            sum_usd += 0
        elif age >= 3 and age <= 12:
            sum_usd += 14
        elif age >= 65:
            sum_usd += 18
        else:
            sum_usd += 23
    return sum_usd


def print_price_list() -> None:
    print("Price List:")
    print(
        "Age\t\t\t\tPrice\n<= 2 y.o.\t\t\t$0\n3 to 12 y.o.\t\t\t$14\n>= 65 y.o.\t\t\t$18\nothers\t\t\t\t$23"
    )


def print_program_description() -> None:
    print("\nHi.\n")
    print(
        "This is a toy program that calculates total price of tickets for guestss entering a zoo."
    )
    print(
        "The price is calculated based on the guests age (integer 0 to 120, numbers outside the range are ignored)."
    )
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    print_price_list()
    print("\nTo terminate entering guessts age press Enter in an empty line.")
    guest_ages = get_guest_ages_from_user()
    print("\nRemoving incorrect ages from the list (if any).")
    guest_ages = filter_out_incorrect_ages(guest_ages)
    print("Calculating total price of entry tickets for the group of guessts.")
    print(
        "\nThe tickets will cost ${0} in total".format(
            calculate_total_price_usd(guest_ages)
        )
    )
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
