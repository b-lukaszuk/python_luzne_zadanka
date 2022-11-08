import os
import re
import sys
from typing import Dict


def is_file_ok(file_path: str) -> bool:
    return os.path.exists(file_path) and os.path.isfile(file_path)


# assumption one word per line, no special characters
# read words are lowercased
def get_correctly_typed_words(file_path: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    with open(file_path, "r") as f:
        result = {word.strip().lower(): 1 for word in f}
    return result


def get_words_to_spellcheck(file_path: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    with open(file_path, "r") as f:
        result = {
            re.sub("[^a-z']", "", word.strip().lower()): 1
            for line in f
            for word in re.split(r"\s", line)
        }
    return result


def get_misspelled_words(
    words_to_spellcheck: Dict[str, int], correctly_typed_words: Dict[str, int]
) -> Dict[str, int]:
    return {
        word_to_check: 1
        for word_to_check in words_to_spellcheck
        if word_to_check not in correctly_typed_words
    }


def main() -> None:
    terminate_program: bool = False
    correct_words: Dict[str, int] = {}
    words_to_spellcheck: Dict[str, int] = {}
    misspelled_words: Dict[str, int] = {}
    for file_path in sys.argv[1:]:
        if not is_file_ok(file_path):
            print("Cannot find '{0}'. Is this a valid file?".format(file_path))
            terminate_program = True
    if len(sys.argv) != 3:
        print("Incorrect number of arguments.")
        terminate_program = True
    if not terminate_program:
        words_to_spellcheck = get_words_to_spellcheck(sys.argv[1])
        correct_words = get_correctly_typed_words(sys.argv[2])
        misspelled_words = get_misspelled_words(words_to_spellcheck, correct_words)
        print("\nMisspelled words:")
        for misspelled_word in misspelled_words:
            if misspelled_word.strip() != "":
                print(misspelled_word)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
