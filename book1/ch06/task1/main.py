# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple
import random


def throw_a_dice(n_times: int) -> List[int]:
    random.seed(None)
    return random.choices(population=range(1, 7), k=n_times)


def throw_two_dice(n_times: int) -> List[Tuple[int, int]]:
    return list(zip(throw_a_dice(n_times), throw_a_dice(n_times)))


def throw_two_dice_and_get_throws_counts(n_times: int) -> Dict[int, int]:
    counts: Dict[int, int] = {}
    for double_throw in throw_two_dice(n_times):
        sum_of_dots: int = sum(double_throw)
        if sum_of_dots in counts:
            counts[sum_of_dots] += 1
        else:
            counts[sum_of_dots] = 1
    return counts


def get_sums_of_all_possible_two_dice_throws() -> List[int]:
    return [sum((t1, t2)) for t1 in range(1, 7) for t2 in range(1, 7)]


# returns probability in decimal (as in textbooks for statistics)
def get_theor_probab_of_two_dice_throw(
    lookup_two_dice_sum: int, sums_of_all_possible_throws: List[int]
) -> float:
    desired_sums: List[int] = [
        throw_result
        for throw_result in sums_of_all_possible_throws
        if throw_result == lookup_two_dice_sum
    ]
    return len(desired_sums) / len(sums_of_all_possible_throws)


# returns probabilities decimals (as in textbooks for statistics)
def get_theor_probabilities_for_all_two_dice_throws() -> Dict[int, float]:
    sums_of_all_possible_throws: List[int] = get_sums_of_all_possible_two_dice_throws()
    probabilities: Dict[int, float] = {
        i: get_theor_probab_of_two_dice_throw(i, sums_of_all_possible_throws)
        for i in range(2, 13)
    }
    return probabilities


# returns probability in decimal (as in textbooks for statistics)
def get_observed_probab_for_all_two_dice_throws(
    throw_counts: Dict[int, int]
) -> Dict[int, float]:
    total_throws: int = sum([throw_counts[key] for key in throw_counts.keys()])
    probabilities: Dict[int, float] = {
        key: throw_counts[key] / total_throws for key in throw_counts.keys()
    }
    return probabilities


def perform_simulation_and_declare_results(n_times: int = 1000) -> None:
    throws_counts: Dict[int, int] = throw_two_dice_and_get_throws_counts(n_times)
    observed_probab: Dict[int, float] = get_observed_probab_for_all_two_dice_throws(
        throws_counts
    )
    theoret_probab: Dict[int, float] = get_theor_probabilities_for_all_two_dice_throws()
    keys: List[int] = sorted(list(throws_counts.keys()))
    print("Total\t\tProb(%, simul.)\t\tProb(%, theor.)")
    for key in keys:
        print(
            "{0}\t\t{1:.2f}\t\t\t{2:.2f}".format(
                key, observed_probab[key] * 100, theoret_probab[key] * 100
            )
        )


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It simulates 1000 throws of two dice.")
    print("Next, it calculates the observed probabilities for the throws.")
    print("It writes down the observed and theoretical probabilities side by side.")
    print("The results are print on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    print("Performing simulation of 1000 two dice throws.")
    print("Please be patient this may take a while.")
    print("\nResults:")
    perform_simulation_and_declare_results()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
