from typing import List


def get_edit_distance(str_s: str, str_t: str) -> int:
    if len(str_s) == 0:
        return len(str_t)
    elif len(str_t) == 0:
        return len(str_s)
    else:
        cost: int = 0
        if str_s[-1] != str_t[-1]:
            cost = 1
        d1: int = get_edit_distance(str_s[:-1], str_t) + 1
        d2: int = get_edit_distance(str_s, str_t[:-1]) + 1
        d3: int = get_edit_distance(str_s[:-1], str_t[:-1]) + cost
        return min(d1, d2, d3)


def get_input_from_user() -> List[str]:
    words: List[str] = []
    word: str = ""
    while True:
        word: str = input("\nEnter a word: ")
        if word.strip() != "" and " " not in word:
            words.append(word)
        else:
            print("Incorrect input. Try again.")
        if len(words) == 2:
            break
    return words


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It asks user to enter two words.")
    print("Then it calculates the so called edit distance between them.")
    print("The result is displayed on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        word1, word2 = get_input_from_user()
        print(
            "\nEdit distance between '{0}' and '{1}' is {2}".format(
                word1, word2, get_edit_distance(word1, word2)
            )
        )
        end_program = input("\n\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
