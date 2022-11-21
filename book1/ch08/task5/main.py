from typing import List, Tuple, TypeVar

T = TypeVar("T")


def encode_run_length(
    list: List[T], acc: List[Tuple[T, int]] = []
) -> List[Tuple[T, int]]:
    if len(list) == 0:
        return acc
    elif len(acc) == 0:
        return encode_run_length(list[1:], [(list[0], 1)])
    elif acc[-1][0] == list[0]:
        acc[-1] = (list[0], acc[-1][1] + 1)
        return encode_run_length(list[1:], acc)
    else:
        acc.append((list[0], 1))
        return encode_run_length(list[1:], acc)


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It performs run length encoding on a list.")
    print("The result is displayed on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()

    list_a: List[str] = list("aaaccabbbbbbbea")
    list_b: List[int] = [1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 3, 3, 3]
    print("\nExample A: {0}".format(list_a))
    print("Example A encoded: {0}".format(encode_run_length(list_a)))
    print("\nExample b: {0}".format(list_b))
    print("Example b encoded: {0}".format(encode_run_length(list_b)))

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
