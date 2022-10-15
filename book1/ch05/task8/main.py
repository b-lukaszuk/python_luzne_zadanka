# -*- coding: utf-8 -*-

from typing import List


def get_primes_upto(upto: int, upper_limit: int = 1000) -> List[bool]:
    if upto <= 1 or upto > upper_limit:
        raise ValueError("Prime numbers must be in range 2 to {0}".format(upper_limit))
    pointer: int = 2
    primes: List[bool] = [True] * (upto + 1)
    while pointer < upto:
        for i in range(pointer + 1, upto + 1):
            if primes[i] and i % pointer == 0:
                primes[i] = False
        pointer += 1
    return primes


def print_primes_upto(upto: int) -> None:
    primes: List[bool] = get_primes_upto(upto)
    for i in range(2, len(primes)):
        if primes[i]:
            print(i, end=", ")
    print("\b \b\b \b")


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It lists prime numbers upto a certain limit.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    upto: int = 200
    print("Listing all prime numbers upto {0}.\n".format(upto))
    print_primes_upto(upto)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
