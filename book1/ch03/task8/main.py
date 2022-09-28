# -*- coding: utf-8 -*-

from typing import List
import random

# 0 - heads, 1 - tails
def toss_a_coin() -> int:
    random.seed(a=None)
    return random.randint(0, 1)


def are_n_same_elts_in_row(ints: List[int], n: int = 3) -> bool:
    if len(ints) == 0:
        return False
    if n == 1:
        return True
    count: int = 1
    prev_elt: int = ints[0]
    for i in range(1, len(ints)):
        if ints[i] == prev_elt:
            count += 1
            if count == n:
                return True
        else:
            count = 1
            prev_elt = ints[i]
    return False


def binary_to_heads_or_tails(binary_0_or_1: int) -> str:
    return "H" if binary_0_or_1 == 0 else "T"


def get_list_of_heads_and_tails(binaries_0s_1s: List[int]) -> str:
    return " ".join([binary_to_heads_or_tails(binary) for binary in binaries_0s_1s])


def declare_tosses(binaries_0s_1s: List[int]) -> None:
    print(" ".join(get_list_of_heads_and_tails(binaries_0s_1s)), end=" ")
    print("({0} flips)".format(len(binaries_0s_1s)))


def get_coin_tosses_until_n_in_row(n: int = 3) -> List[int]:
    tosses: List[int] = []
    while not are_n_same_elts_in_row(tosses, n):
        tosses.append(toss_a_coin())
    return tosses


def get_average(ints: List[int]) -> float:
    return sum(ints) / len(ints)


def declare_average_tosses_needed(list_of_binaries: List[List[int]]) -> None:
    counts: List[int] = [len(binary) for binary in list_of_binaries]
    print("On average {0:.2f} flips were needed.".format(get_average(counts)))


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that performes simulations of coin tosses.")
    print("Each simulation is performed until three heads or tails in a row occur.")
    print("The result of is print to the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    number_of_simulations: int = 10
    simulations: List[List[int]] = []
    print_program_description()
    for i in range(number_of_simulations):
        simulations.append(get_coin_tosses_until_n_in_row())
        print("\nSimulation {0}:".format(i + 1))
        declare_tosses(simulations[i])
    print()
    declare_average_tosses_needed(simulations)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
