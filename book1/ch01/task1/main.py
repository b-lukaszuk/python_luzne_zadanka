# -*- coding: utf-8 -*-

import math
from typing import Callable, List, TypedDict


class Custom_Function(TypedDict):
    description: str
    fun: Callable[[int, int], float]


my_functions: List[Custom_Function] = [
    {"description": "The sum of {0} and {1}", "fun": lambda a, b: a + b},
    {
        "description": "The difference when {1} is subtracted from {0}",
        "fun": lambda a, b: a - b,
    },
    {"description": "The product of {0} and {1}", "fun": lambda a, b: a * b},
    {"description": "The quotient of {0} divided by {1}", "fun": lambda a, b: a / b},
    {
        "description": "The reminder when {0} is divided by {1}",
        "fun": lambda a, b: a % b,
    },
    {"description": "The result of log10 of {0}", "fun": lambda a, _: math.log10(a)},
    {
        "description": "The result of {0} to the power of {1}",
        "fun": lambda a, b: a ** b,
    },
]


def handleUserInput(name_of_variable: str = "a", default_int: int = 2) -> int:
    users_input: str = input(
        "Enter a value of variable {0} (positive integer) and press enter: ".format(
            name_of_variable
        )
    )
    an_int: int = default_int
    try:
        if int(users_input) <= 0:
            raise ValueError
        an_int = int(users_input)
    except ValueError:
        print("Invalid input. I default to {0}\n".format(default_int))
    return an_int


def print_info_about_fn(fn: Custom_Function, arg1: int, arg2: int) -> None:
    print(fn["description"].format(arg1, arg2))
    print("result: {:.3f}\n".format(fn["fun"](arg1, arg2)))


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a program that reads two integers, a and b, from the user.")
    print("Next it will perform a number of mathematical operations on them.")
    print(
        "The results of the operations (and their descriptions) will be printed to the terminal."
    )
    print("All clear. Then let's begin.\n")


def main() -> None:
    arg_a: int = 2
    arg_b: int = 2
    print_program_description()
    arg_a = handleUserInput("a", arg_a)
    arg_b = handleUserInput("b", arg_b)
    for custom_function in my_functions:
        print_info_about_fn(custom_function, arg_a, arg_b)
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
