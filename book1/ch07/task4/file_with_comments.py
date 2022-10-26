## imports
import os.path
import string
import sys
from typing import Dict, List  # needed for type suggestions


# returns file contents as a single string
def get_file_contents(file_path: str) -> str:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return "".join(lines)


# checking validity of the arguments
def are_sys_argv_ok(sys_argv: List[str]) -> bool:
    return len(sys_argv) == 2 and os.path.isfile(sys_argv[1])


def get_ascii_lowercase_frequencies(text: str) -> Dict[str, int]:
    frequencies: Dict[str, int] = {}
    for character in text:
        if character in string.ascii_lowercase:
            if character in frequencies:
                frequencies[character] += 1
            else:
                frequencies[character] = 1
    return frequencies


def print_ascii_lowercase_frequencies(frequencies: Dict[str, int]) -> None:
    for key in string.ascii_lowercase:
        if key in frequencies:
            print("{0}: {1}".format(key, frequencies[key]))


# print error messages if any
def print_error_msgs_for_sys_argv(sys_argv: List[str]) -> None:
    print()
    if len(sys_argv) != 2:
        print("Incorrect number of arguments sent to program.")
    elif not os.path.isfile(sys_argv[1]):
        print("File '{0}' does not exist.".format(sys_argv[1]))
    print("Terminating program.\n")  # prints always when the function runs


def main() -> None:
    if not are_sys_argv_ok(sys.argv):
        print_error_msgs_for_sys_argv(sys.argv)
    else:
        print("\nReading contents of '{0}'".format(sys.argv[1]))
        file_contents: str = get_file_contents(sys.argv[1])
        print("Calculating frequencies of characters", end=" ")
        print("(case insensitive, ascii_lowercase)\n")
        print("Result:")
        print_ascii_lowercase_frequencies(
            get_ascii_lowercase_frequencies(file_contents.lower())
        )
        print("\nThat's all. Goodbye!")


# runs code in main only if the file name is evoked from terminal
if __name__ == "__main__":
    main()
