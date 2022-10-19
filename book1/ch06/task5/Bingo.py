# -*- coding: utf-8 -*-

import random
from typing import Any, Dict, List


class Bingo:
    def __init__(self) -> None:
        self.__bingo: Dict[str, List[int]] = self.__get_random_digits_in_bingo()

    def __str__(self) -> str:
        return self.__get_formatted_bingo()

    def __repr__(self) -> str:
        return self.__str__()

    # returns dict with key columns identificator and digits (values) in List[int]
    # middle of the card [2, 2] is empty (it is always considered to be marked)
    def __get_random_digits_in_bingo(self) -> Dict[str, List[int]]:
        start: int = 1
        columns: Dict[str, List[int]] = {}
        for column in "bingo":
            random.seed(None)
            columns[column] = random.sample(population=range(start, start + 15), k=5)
            if column == "n":
                columns[column][2] = 0
            start += 15
        return columns

    def __r_pad_entry(self, entry: Any, pad: str = " ", final_len: int = 3) -> str:
        return "{0}{1}".format(
            entry,
            pad * (final_len - len(str(entry))),
        )

    def __r_pad_list(
        self, a_list: List[Any], pad: str = " ", elt_final_len: int = 3
    ) -> List[str]:
        return [self.__r_pad_entry(elt, pad, elt_final_len) for elt in a_list]

    def __format_list_to_row(self, padded_list: List[Any], col_sep: str = "|") -> str:
        return "{0}{1}{2}".format(col_sep, col_sep.join(padded_list), col_sep)

    def __get_row(self, row_id: int) -> List[int]:
        row: List[int] = []
        if row_id not in range(5):
            raise ValueError("row_id must be in range(0, 5)")
        else:
            for key in "bingo":
                row.append(self.__bingo[key][row_id])
        return row

    # row_id range(-1, 5), -1 for header
    def __get_formatted_row(self, row_id: int) -> str:
        if row_id == -1:
            return self.__format_list_to_row(self.__r_pad_list(list("BINGO")), " ")
        else:
            return self.__format_list_to_row(self.__r_pad_list(self.__get_row(row_id)))

    def __get_formatted_bingo(self) -> str:
        rows: List[str] = [self.__get_formatted_row(i) + "\n" for i in range(-1, 5)]
        row_separator: str = "-" * (len(rows[1]) - 1) + "\n"
        return "\n" + row_separator.join(rows) + row_separator

    def __get_sums_of_columns(self) -> List[int]:
        return [sum(self.__bingo[col_id]) for col_id in "bingo"]

    def __is_any_col_marked(self) -> bool:
        return any(elt == 0 for elt in self.__get_sums_of_columns())

    def __get_sums_of_rows(self) -> List[int]:
        return [sum(self.__get_row(row_id)) for row_id in range(5)]

    def __is_any_row_marked(self) -> bool:
        return any(elt == 0 for elt in self.__get_sums_of_rows())

    def __get_diagonal(self, backslash: bool = True) -> List[int]:
        direction: List[int] = (
            list(range(0, 5)) if backslash else list(range(0, 5))[::-1]
        )
        col_ids: List[str] = list("bingo")
        diagonal: List[int] = []
        for i in range(len(col_ids)):
            diagonal.append(self.__bingo[col_ids[i]][direction[i]])
        return diagonal

    def __get_sums_of_diagonals(self) -> List[int]:
        return [sum(self.__get_diagonal()), sum(self.__get_diagonal(False))]

    def __is_any_diagonal_marked(self) -> bool:
        return any(elt == 0 for elt in self.__get_sums_of_diagonals())

    def is_bingo_winning(self) -> bool:
        return (
            self.__is_any_col_marked()
            or self.__is_any_row_marked()
            or self.__is_any_diagonal_marked()
        )

    def mark_number_if_exists(self, number: int) -> None:
        if 0 < number < 76:
            for col_id in "bingo":
                for row_id in range(5):
                    if self.__bingo[col_id][row_id] == number:
                        self.__bingo[col_id][row_id] = 0
