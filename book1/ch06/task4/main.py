# -*- coding: utf-8 -*-

import copy
import random
from typing import Any, Dict, List

# returns dict with key columns identificator and digits (values) in List[int]
# middle of the card [2, 2] is empty (it is always considered to be marked)
def get_digits_in_bingo() -> Dict[str, List[int]]:
    start: int = 1
    columns: Dict[str, List[int]] = {}
    for column in "bingo":
        random.seed(None)
        columns[column] = random.sample(population=range(start, start + 15), k=5)
        if column == "n":
            columns[column][2] = 0
        start += 15
    return columns


def r_pad_entry(entry: Any, pad: str = " ", final_len: int = 3) -> str:
    return "{0}{1}".format(
        entry,
        pad * (final_len - len(str(entry))),
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
    result: str = "\n"
    for i in range(-1, 5):
        result += get_formatted_row(bingo, i) + "\n"
        result += "-" * 21 + "\n"
    return result


def mark_random_column(bingo: Dict[str, List[int]]) -> Dict[str, List[int]]:
    random.seed(None)
    col_id: str = random.choice(list("bingo"))
    result: Dict[str, List[int]] = copy.deepcopy(bingo)
    result[col_id] = [0] * 5
    return result


def mark_random_row(bingo: Dict[str, List[int]]) -> Dict[str, List[int]]:
    result: Dict[str, List[int]] = copy.deepcopy(bingo)
    random.seed(None)
    row_id: int = random.choice(range(5))
    for col_id in "bingo":
        result[col_id][row_id] = 0
    return result


def mark_random_diagonal(bingo: Dict[str, List[int]]) -> Dict[str, List[int]]:
    result: Dict[str, List[int]] = copy.deepcopy(bingo)
    random.seed(None)
    direction: List[int] = random.choice([list(range(0, 5)), list(range(4, -1, -1))])
    col_ids: List[str] = list("bingo")
    for i in range(len(col_ids)):
        result[col_ids[i]][direction[i]] = 0
    return result


def get_sums_of_columns(bingo: Dict[str, List[int]]) -> List[int]:
    return [sum(bingo[col_id]) for col_id in "bingo"]


def is_any_col_marked(bingo: Dict[str, List[int]]) -> bool:
    return any(elt == 0 for elt in get_sums_of_columns(bingo))


def get_sums_of_rows(bingo: Dict[str, List[int]]) -> List[int]:
    return [sum(get_row(bingo, row_id)) for row_id in range(5)]


def is_any_row_marked(bingo: Dict[str, List[int]]) -> bool:
    return any(elt == 0 for elt in get_sums_of_rows(bingo))


def get_diagonal(bingo: Dict[str, List[int]], backslash: bool = True) -> List[int]:
    direction: List[int] = list(range(0, 5)) if backslash else list(range(0, 5))[::-1]
    col_ids: List[str] = list("bingo")
    diagonal: List[int] = []
    for i in range(len(col_ids)):
        diagonal.append(bingo[col_ids[i]][direction[i]])
    return diagonal


def get_sums_of_diagonals(bingo: Dict[str, List[int]]) -> List[int]:
    return [sum(get_diagonal(bingo)), sum(get_diagonal(bingo, False))]


def is_any_diagonal_marked(bingo: Dict[str, List[int]]) -> bool:
    return any(elt == 0 for elt in get_sums_of_diagonals(bingo))


def is_bingo_winning(bingo: Dict[str, List[int]]) -> bool:
    return (
        is_any_col_marked(bingo)
        or is_any_row_marked(bingo)
        or is_any_diagonal_marked(bingo)
    )


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It checks if a bingo card (American version) is winning.")
    print("By winning we mean either column, row or diagonal is all marked.")
    print("The program generates random bingo and marks random fields.")
    print("(random columns, rows, and diagonals)")
    print("The program marks bingo fields with zeros.")
    print("Then it performs the check.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()
    bingo: Dict[str, List[int]] = get_digits_in_bingo()
    bingos: List[Dict[str, List[int]]] = [
        bingo,
        mark_random_column(bingo),
        mark_random_row(bingo),
        mark_random_diagonal(bingo),
    ]
    for i in random.sample(population=range(len(bingos)), k=len(bingos)):
        print(get_formatted_bingo(bingos[i]))
        print("Is winning? {0}".format(is_bingo_winning(bingos[i])))
        print("\n\n========")
    print("That's all. Goodbye!\n")


if __name__ == "__main__":
    main()
