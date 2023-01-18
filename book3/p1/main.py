#!/usr/bin/env python3

import random

def get_rand_3dig_num() -> int:
    random.seed(a=None)
    return random.randint(100, 999)

def is_bagles(guess: int, secret_num: int) -> bool:
    g: str = str(guess)
    sn: str = str(secret_num)
    return not any([c in sn for c in g])

def get_except(text: str, ind: int) -> str:
    result: str = ""
    for i in range(len(text)):
        if ind != i:
            result = result+text[i]
    return result

def is_pico(guess: int, secret_num: int) -> bool:
    g: str = str(guess)
    sn: str = str(secret_num)
    for i in range(len(sn)):
        if g[i] in get_except(sn, i):
            return True
    return False

def is_fermi(guess: int, secret_num: int) -> bool:
    g: str = str(guess)
    sn: str = str(secret_num)
    for i in range(len(sn)):
        if g[i] == sn[i]:
            return True
    return False

def main() -> None:
    print("Project 1.")
    print("Status: Not finished.")

if __name__ == "__main__":
    main()
