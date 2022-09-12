# -*- coding: utf-8 -*-

from typing import List, Dict

# available coins and their values, sorted (desc)
available_coins: List[Dict[str, int]] = [
    {"toonie": 200},
    {"loonie": 100},
    {"quarter": 25},
    {"dime": 10},
    {"nickel": 5},
    {"penny": 1},
]


def can_be_subtracted_from_total(amount: int, total: int) -> bool:
    return amount <= total


# available_coins needs to be sorted in descending order
def get_change(
    sum_to_change: int,
    available_coins: List[Dict[str, int]] = available_coins,
) -> Dict[str, int]:
    change: Dict[str, int] = {}
    for coin in available_coins:
        for (coin_name, coin_value) in coin.items():
            while can_be_subtracted_from_total(coin_value, sum_to_change):
                sum_to_change -= coin_value
                if coin_name in change:
                    change[coin_name] += 1
                else:
                    change[coin_name] = 1
    return change


def get_input_from_user(default_on_error: int = 1234) -> int:
    user_input_str: str = input(
        "Enter the amount of money (integer) in cents: "
    )
    try:
        user_input_int: int = int(user_input_str)
        return user_input_int
    except ValueError:
        print("Invalid input. I default to 1234")
        return default_on_error


def print_program_description() -> None:
    print("\nHi.\n")
    print("This program reads the number of cents (integer) from the user")
    print("Next, it gives the change (using as few coins as possible)")
    print("Available coins (unlimited supply):")
    print("toonie ($2), loonie ($1), quarter (25/100th of $1),")
    print(
        "dime (10/100th of $1), nickel (5/100th of $1), penny (1/100th of $1)"
    )
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()

    sum_to_change = get_input_from_user()
    print("\nChanging {0} cents".format(sum_to_change))
    print("Result: {0}".format(get_change(sum_to_change)))

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
