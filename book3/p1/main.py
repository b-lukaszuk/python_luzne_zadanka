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


def print_hint(guess: int, secret_num: int) -> None:
    if is_bagles(guess, secret_num):
        print("Bagles.")
    if is_fermi(guess, secret_num):
        print("Fermi.")
    if is_pico(guess, secret_num):
        print("Pico.")


def print_game_description() -> None:
    print("Welcome to the game of Bagles.")
    print("In a moment I will think of a three digit integer.")
    print("You got nine guesses to figure it out.")
    print("After each guess You will get a hint.")
    print("'Pico' when youg guess has a correct digit in the wrong place.")
    print("'Fermi' when youg guess has a correct digit in the correct place.")
    print("'Bagles' when youg guess has no correct digits.")
    print("Ok, let's begin. What is my number?")
    _ = input("Press Enter to continue.")


def main() -> None:
    print("Project 1.")
    print("Status: Not finished.")


if __name__ == "__main__":
    main()
