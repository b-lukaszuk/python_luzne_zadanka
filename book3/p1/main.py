#!/usr/bin/env python3

import random


def get_rand_3dig_num() -> int:
    random.seed(a=None)
    return random.randint(100, 999)


def is_bagles(guess: int, secret_num: int) -> bool:
    return not any([c in str(secret_num) for c in str(guess)])


def get_except(text: str, ind: int) -> str:
    return "".join([c for (i, c) in enumerate(text) if i != ind])


def is_pico(guess: int, secret_num: int) -> bool:
    g: str = str(guess)
    sn: str = str(secret_num)
    return any([c in get_except(sn, i) for (i, c) in enumerate(g)])


def is_fermi(guess: int, secret_num: int) -> bool:
    g: str = str(guess)
    sn: str = str(secret_num)
    return any([g[i] == sn[i] for i in range(len(sn))])


def is_num_ok(guess: str) -> bool:
    try:
        num: int = int(guess)
        return 99 < num < 1000
    except ValueError:
        return False


def get_user_input() -> int:
    guess: str = ""
    while not is_num_ok(guess):
        print("Enter your guess.")
        guess = input("Enter 3 digit integer and press Enter: ")
    return int(guess)


def main() -> None:
    print("Project 1.")
    print("Status: Not finished.")


if __name__ == "__main__":
    main()
