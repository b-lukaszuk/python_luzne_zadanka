# -*- coding: utf-8 -*-

from Bingo import Bingo
import random
from typing import Any, Dict, List


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It checks if a bingo card (American version) is winning.")
    print("By winning we mean either column, row or diagonal is all marked.")
    print("The program generates random bingo and marks random fields.")
    print("(random columns, rows, and diagonals)")
    print("The program marks bingo fields with zeros.")
    print("Then it performs the check.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()
    print("That's all. Goodbye!\n")


if __name__ == "__main__":
    main()
