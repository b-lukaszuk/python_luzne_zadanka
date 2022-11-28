# -*- coding: utf-8 -*-

import random


def get_sum_of_n_nn_nnn(n: int) -> int:
    sum: int = 0
    for i in range(1, 4):
        sum += n ** i
    return sum


def main() -> None:
    random.seed(a=None)
    n: int = random.randint(1, 4)
    print("Sum(n, nn, nnn) examples:")
    print("n = {0}".format(n))
    print("Sum(n, nn, nnn) = {0}".format(get_sum_of_n_nn_nnn(n)))
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
