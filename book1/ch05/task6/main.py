# -*- coding: utf-8 -*-

from typing import List

# math_expression musn't contain spaces
def get_indexes_of_token_separator(
    math_expression: str, sep_character: str
) -> List[int]:
    indexes: List[int] = []
    for i in range(len(math_expression)):
        if math_expression[i] == sep_character:
            # +- may be operator or indicate positive or negative numbers
            if sep_character not in "+-":
                indexes.append(i)
            elif (i - 1) != -1 and math_expression[i - 1] in "0123456)":
                indexes.append(i)
    return indexes


# math_expression musn't contain spaces
def get_indexes_of_token_separators(
    math_expression: str, separators: str = "()+-*/"
) -> List[int]:
    indexes: List[int] = []
    for separator in separators:
        indexes.extend(get_indexes_of_token_separator(math_expression, separator))
    return indexes


def split_text_at(text: str, indexes: List[int]) -> List[str]:
    result: List[str] = []
    start_ind: int = 0
    end_ind: int = indexes[0]
    for ind in indexes:
        end_ind = ind
        result.append(text[start_ind:end_ind])
        result.append(text[end_ind : (end_ind + 1)])
        start_ind = end_ind + 1
    result.append(text[start_ind:])
    return [res for res in result if res != ""]


def get_tokens(math_expression: str, separators: str = "()+-*/") -> List[str]:
    expression_no_spaces = math_expression.replace(" ", "")
    indexes: List[int] = get_indexes_of_token_separators(
        expression_no_spaces, separators
    )
    indexes.sort()
    tokens: List[str] = split_text_at(expression_no_spaces, indexes)
    # not sure if -/+ before parenthesis should go separetley of ( or together
    # here is together (since it is not separate operator but negation) like with numbers
    if tokens[0] in "+-" and tokens[1] in "(":
        tokens = [tokens[0] + tokens[1]] + tokens[2:]
    return tokens


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that splits simple math formulas to tokens.")
    print(
        "The tokens are: a parenthesis, an operator, or a number with an optional leading + or -."
    )
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    simple_equations: List[str] = [
        "1 + 2 + 3",
        "3 - 4 * 5",
        "+3 - 4 * 5",
        "-8 / 2 * 3",
        "2 * -18",
        "(3 + 2) * 4 - (12 - 3)",
        "-(3 / 2) * 4 - (12 - +3)",
    ]
    for equation in simple_equations:
        print("\nEquation: {0}".format(equation))
        print("Tokens: {0}".format(get_tokens(equation)))
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
