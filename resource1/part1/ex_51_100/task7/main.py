# -*- coding: utf-8 -*-

import socket


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It prints the name of the host on which it is running.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    print("-" * 3)
    print("Hostname: {0}".format(socket.gethostname()))
    print("-" * 3)

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
