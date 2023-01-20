#!/usr/bin/env python3


import random
from typing import List


def get_rand_3dig_num() -> int:
    random.seed(a=None)
    return random.randint(100, 999)


def is_bagles(guess: int, secret_num: int) -> bool:
    return not any([c in str(secret_num) for c in str(guess)])


def get_except(text: str, ind: int) -> str:
    return "".join([c for (i, c) in enumerate(text) if i != ind])


def is_pico(guess: int, secret_num: int) -> List[bool]:
    g: str = str(guess)
    sn: str = str(secret_num)
    return [c in get_except(sn, i) for (i, c) in enumerate(g)]


def is_fermi(guess: int, secret_num: int) -> List[bool]:
    g: str = str(guess)
    sn: str = str(secret_num)
    return [g[i] == sn[i] for i in range(len(sn))]


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
    bagles: bool = is_bagles(guess, secret_num)
    fermis: List[bool] = is_fermi(guess, secret_num)
    picos: List[bool] = is_pico(guess, secret_num)
    if bagles:
        print("Bagles.")
    if any(fermis):
        print(["Fermi" for f in fermis if f])
    if any(picos):
        print(["Pico" for p in picos if p])


def run_game_loop() -> None:
    secret_num: int = get_rand_3dig_num()
    guess: int = 0
    counter: int = 0
    while (guess != secret_num) and (counter < 9):
        print("\n---Guess {0} of 9---".format(counter+1))
        guess = get_user_input()
        print_hint(guess, secret_num)
        counter += 1
    print("\nGame Over!")
    if guess != secret_num:
        print("You lost.")
    else:
        print("You won.")
    print("My secret number was {0}".format(secret_num))


def print_game_description() -> None:
    print("Welcome to the game of Bagles.")
    print("In a moment I will think of a three digit integer.")
    print("You got nine guesses to figure it out.")
    print("After each guess You will get a hint.")
    print("'Pico' when your guess has a correct digit in the wrong place.")
    print("'Fermi' when your guess has a correct digit in the correct place.")
    print("'Bagles' when your guess has no correct digits.")
    print("Ok, let's begin. What is my number?")
    _ = input("Press Enter to continue.")


def main() -> None:
    print_game_description()
    run_game_loop()
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
