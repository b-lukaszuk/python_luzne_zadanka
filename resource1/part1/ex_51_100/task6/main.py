# -*- coding: utf-8 -*-

import time


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program that prints the system time.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    print("-" * 3)
    print("Time in seconds since epoch: {0}".format(time.time()))
    print("Current time: {0}".format(time.ctime()))
    print("-" * 3)

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
