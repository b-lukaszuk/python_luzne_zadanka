# -*- coding: utf-8 -*-

from typing import List


def lpad(text: str, pad_char: str = "0", final_len: int = 5) -> str:
    result: str = text
    while len(result) < final_len:
        result = pad_char + result
    return result


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It generates the examples of padding some text with zeros.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    examples: List[str] = ["hello", "there", "tom", "molly"]
    for example in examples:
        print("-" * 3)
        print("custom lpad({0})  : '{1}'".format(example, lpad(example, "0", 10)))
        print("build-in lpad({0}): '{1:0>10}'".format(example, example))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
