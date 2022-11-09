import os
import re
import sys
from typing import Dict, List


def is_file_ok(file_path: str) -> bool:
    return os.path.exists(file_path) and os.path.isfile(file_path)


def are_argv_ok_print_messages_and_get_decision(sys_argv: List[str]) -> bool:
    print("\nProgram running. Evaluating entered arguments.")
    if len(sys_argv) != 3:
        print("Incorrect number of arguments.")
        return False
    for file_path in sys_argv[1:]:
        if not is_file_ok(file_path):
            print("Cannot find '{0}'. Is this a valid file?".format(file_path))
            return False
    print("Everything looks fine.\n")
    return True


# assumption one word per line, no special characters
# read words are lowercased
def get_correctly_typed_words(file_path: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    with open(file_path, "r") as f:
        result = {word.strip().lower(): 1 for word in f}
    return result


# assumption more than one word per line, with special characters (,.!?, etc.)
# read words are lowercased
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
        if word_to_check not in correctly_typed_words and word_to_check != ""
    }


def print_misspelled_words(
    words_to_spellcheck: Dict[str, int], correctly_typed_words: Dict[str, int]
) -> None:
    misspelled_words: Dict[str, int] = get_misspelled_words(
        words_to_spellcheck, correctly_typed_words
    )
    print("\nMisspelled words:")
    if misspelled_words:
        for misspelled_word in misspelled_words:
            if misspelled_word.strip() != "":
                print(misspelled_word)
    else:
        print("No misspelled words found.")


def main() -> None:
    terminate_program: bool = not are_argv_ok_print_messages_and_get_decision(sys.argv)
    correct_words: Dict[str, int] = {}
    words_to_spellcheck: Dict[str, int] = {}
    if terminate_program:
        print("Nothing to do. Terminating program.")
    else:
        print("Reading words to spellcheck from file '{0}'".format(sys.argv[1]))
        words_to_spellcheck = get_words_to_spellcheck(sys.argv[1])
        print("Reading reference words from file '{0}'".format(sys.argv[2]))
        correct_words = get_correctly_typed_words(sys.argv[2])
        print("Searching for misspelled words (case insensitive search).")
        print_misspelled_words(words_to_spellcheck, correct_words)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
