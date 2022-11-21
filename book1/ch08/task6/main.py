from typing import List, Tuple, TypeVar

T = TypeVar("T")


def decode_run_length(to_decode: List[Tuple[T, int]], acc: List[T] = []) -> List[T]:
    if len(to_decode) == 0:
        return acc
    if to_decode[0][1] <= 0:
        return decode_run_length(to_decode[1:], acc)
    if len(acc) == 0:
        to_decode = to_decode[:]  # prevents modificaion of original list (args)
        to_decode[0] = (to_decode[0][0], to_decode[0][1] - 1)
        return decode_run_length(to_decode, [to_decode[0][0]])
    else:
        to_decode[0] = (to_decode[0][0], to_decode[0][1] - 1)
        acc.append(to_decode[0][0])
        return decode_run_length(to_decode, acc)


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It performs run length decoding on a to_decode.")
    print("The result is displayed on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()

    list_a: List[Tuple[str, int]] = [("all", 2), ("is", 3), ("good", 1)]
    list_b: List[Tuple[int, int]] = [(1, 1), (2, 2), (4, 4), (5, 2)]
    print("\nExample A: {0}".format(list_a))
    print("Example A decoded: {0}".format(decode_run_length(list_a)))
    print("\nExample b: {0}".format(list_b))
    print("Example b decoded: {0}".format(decode_run_length(list_b)))

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
