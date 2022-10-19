# -*- coding: utf-8 -*-

import random
from typing import Any, Dict, List

# returns dict with key columns identificator and digits (values) in List[int]
# - 99 for middle of the card [2, 2]
def get_digits_in_bingo() -> Dict[str, List[int]]:
    start: int = 1
    columns: Dict[str, List[int]] = {}
    for column in "bingo":
        random.seed(None)
        columns[column] = random.sample(population=range(start, start + 15), k=5)
        # middle of a bingo card is empty (free space in the middle of the card)
        if column == "n":
            columns[column][2] = -99
        start += 15
    return columns


def r_pad_entry(entry: Any, pad: str = " ", final_len: int = 3) -> str:
    adjusted_entry: str = "  " if str(entry) == "-99" else str(entry)
    return "{0}{1}".format(
        adjusted_entry,
        pad * (final_len - len(str(adjusted_entry))),
    )


def r_pad_list(a_list: List[Any], pad: str = " ", elt_final_len: int = 3) -> List[str]:
    return [r_pad_entry(elt, pad, elt_final_len) for elt in a_list]


def format_list_to_row(padded_list: List[Any], col_sep: str = "|") -> str:
    return "{0}{1}{2}".format(col_sep, col_sep.join(padded_list), col_sep)


def get_row(bingo: Dict[str, List[int]], row_id: int) -> List[int]:
    row: List[int] = []
    if row_id not in range(5):
        raise ValueError("row_id must be in range(0, 5)")
    else:
        for key in "bingo":
            row.append(bingo[key][row_id])
    return row


# row_id range(-1, 5), -1 for header
def get_formatted_row(bingo: Dict[str, List[int]], row_id: int) -> str:
    if row_id == -1:
        return format_list_to_row(r_pad_list(list("BINGO")), " ")
    else:
        return format_list_to_row(r_pad_list(get_row(bingo, row_id)))


def get_formatted_bingo(bingo: Dict[str, List[int]]) -> str:
    rows: List[str] = [get_formatted_row(bingo, i) + "\n" for i in range(-1, 5)]
    row_separator: str = "-" * (len(rows[1]) - 1) + "\n"
    return "\n" + row_separator.join(rows) + row_separator


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It generates a random bingo card (American version).")
    print("The result is printed on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()
    bingo: Dict[str, List[int]] = get_digits_in_bingo()
    print(get_formatted_bingo(bingo))
    print("That's all. Goodbye!\n")


if __name__ == "__main__":
    main()
