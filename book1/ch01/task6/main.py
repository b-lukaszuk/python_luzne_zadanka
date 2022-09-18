# -*- coding: utf-8 -*-


def isNumBetween(num: float, minIncl: float, maxIncl: float) -> bool:
    return (num >= minIncl) and (num <= maxIncl)


def get_input_from_user(
    min_input: int = 1,
    max_input: int = 500,
    default_on_error: int = 5,
) -> int:
    print("Enter the number of a day old bread loaves you want to buy")
    input_str: str = input(
        "Enter integer from {0} to {1}: ".format(min_input, max_input)
    )
    try:
        input_int: int = int(input_str)
        if not isNumBetween(input_int, min_input, max_input):
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}".format(default_on_error))
        input_int = default_on_error
    return input_int


def print_program_description(loaf_price: float, discount_percent: int) -> None:
    print("\nHi.\n")
    print("This program calculates the total price of bread.")
    print("It asks user for the number of a day old bread loaves he/she wants to buy.")
    print("The regular price of bread loaf is ${price:.2f}.".format(price=loaf_price))
    print(
        "The discount for a day old loaf of bread is {discount:.2f}%.".format(
            discount=discount_percent
        )
    )
    print("All clear. Then let's begin.\n")


def main() -> None:

    loaf_price: float = 3.49
    discount_percent: int = 60
    print_program_description(loaf_price=loaf_price, discount_percent=discount_percent)
    num_of_bread_loaves: int = get_input_from_user()
    regular_price_all_breadloaves: float = num_of_bread_loaves * loaf_price
    price_after_discount_all_breadloaves: float = regular_price_all_breadloaves * (
        1 - discount_percent / 100
    )

    print("\nThe regular price for a breadloaf is ${:.2f}.".format(loaf_price))
    print(
        "Buying {how_many} regular loa(f/ves) costs ${price:.2f}.".format(
            how_many=num_of_bread_loaves, price=regular_price_all_breadloaves
        )
    )
    print(
        "After {discount:.2f}% discount for a day old bread the price for the whole order is ${price:.2f}.".format(
            discount=discount_percent, price=price_after_discount_all_breadloaves
        )
    )

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
