# -*- coding: utf-8 -*-

import random
from typing import Dict, List


# nums must be in range 0 to 9 (incl-incl)
def get_counts(nums_0_upto_9: List[int]) -> Dict[int, int]:
    counts: Dict[int, int] = {num: 0 for num in range(10)}
    for num in nums_0_upto_9:
        if num in counts:
            counts[num] += 1
    return counts


def get_histogram_for_counts(counts_of_nums_0_upto_9: Dict[int, int]) -> str:
    histogram: str = ""
    for num in range(10):
        histogram += str(num) + "| " + "#" * counts_of_nums_0_upto_9[num] + "\n"
    return histogram


def get_list_of_random_ints(list_len: int = 30) -> List[int]:
    random.seed(a=None)
    return random.choices(population=range(10), k=list_len)


def main() -> None:
    integers: List[int] = get_list_of_random_ints()
    counts: Dict[int, int] = get_counts(integers)
    print("\nProgram drawing histogram of list of integers.")
    print("The histogram is drawn in text mode.")
    print("Example:\n")
    print("The list of random integers (0 upto 9):\n{0}".format(integers))
    print("The counts: {0}".format(counts))
    print("\nThe histogram:")
    print(get_histogram_for_counts(counts))
    print("That's all. Goodbye!\n")


if __name__ == "__main__":
    main()
