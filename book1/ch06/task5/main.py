# -*- coding: utf-8 -*-

from Bingo import Bingo
import random
from typing import Dict, List


def get_random_calls() -> List[int]:
    random.seed(None)
    return random.sample(population=range(1, 76), k=75)


def get_number_of_calls_until_bingo_winning() -> int:
    counter: int = 0
    bingo: Bingo = Bingo()
    calls: List[int] = get_random_calls()
    for i in range(len(calls)):
        bingo.mark_number_if_exists(calls[i])
        counter += 1
        if bingo.is_bingo_winning():
            break
    return counter


def get_numbers_of_calls_per_n_bingo_winnings(
    n: int = 1000, display_progress: bool = True
) -> List[int]:
    results: List[int] = []
    for i in range(n):
        if display_progress:
            print("Simulation: {0} of {1}".format(i + 1, n), end="")
            print("\r", end="")
        results.append(get_number_of_calls_until_bingo_winning())
    if display_progress:
        print("\nSimulations completed.")
    return results


def get_average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)


def get_statistics(numbers_of_calls: List[int]) -> Dict[str, float]:
    statistics: Dict[str, float] = {
        "max": max(numbers_of_calls),
        "min": min(numbers_of_calls),
        "average": get_average(numbers_of_calls),
    }
    return statistics


def declare_results(number_of_simulations: int = 1000) -> None:
    print("\nPerforming {0} simulations.".format(number_of_simulations))
    print("Please be patient this may take some time.\n")
    statistics: Dict[str, float] = get_statistics(
        get_numbers_of_calls_per_n_bingo_winnings(number_of_simulations)
    )
    print("\nStatistics:")
    for key in ["min", "max", "average"]:
        print("{0} number of calls: {1:.2f}".format(key, statistics[key]))


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It generates a random bingo card (American version).")
    print("Next it generates random calls and mark the numbers on the card.")
    print("The numbers are marked for as long as the card is deemed winning.")
    print("The number of calls is being recorded.")
    print("Next the program gives statistics for ", end="")
    print("the numbers of calls necessary to win bingo, based on 1000 simulations.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    _: str = input("Press any key to continue")
    number_of_simulations: int = 1000
    declare_results(number_of_simulations)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
