# -*- coding: utf-8 -*-


def print_program_description() -> None:
    print("\nHi.\n")
    print(
        "This is a toy program that print the multiplication table (from 1x1 till 10x10)"
    )
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def print_multiplication_table(minIncl: int = 1, maxIncl: int = 10) -> None:
    # for with h prints header row
    for h in range(minIncl - 1, maxIncl + 1):
        print("" if h == minIncl - 1 else str(h), end="\t")
    print()
    for i in range(minIncl, maxIncl + 1):
        for j in range(minIncl, maxIncl + 1):
            # if for printing header column
            if j == minIncl:
                print(i, end="\t")
            print(i * j, end="\n" if j == maxIncl else "\t")


def main() -> None:
    print_program_description()
    print_multiplication_table()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
