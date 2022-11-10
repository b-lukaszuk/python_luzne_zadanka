import os
import sys
from typing import Generator, List


def is_file_ok(file_path: str) -> bool:
    return os.path.exists(file_path) and os.path.isfile(file_path)


def are_argv_ok_print_messages_and_get_decision(sys_argv: List[str]) -> bool:
    print("\nProgram running. Evaluating entered arguments.")
    if len(sys_argv) != 2:
        print("Incorrect number of arguments.")
        return False
    if not is_file_ok(sys_argv[1]):
        print("Cannot find '{0}'. Is this a valid file?".format(sys_argv[1]))
        return False
    print("Everything looks fine.\n")
    return True


def get_words(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        for line in f:
            if line == "\n":
                yield "\n"
            else:
                for word in line.split():
                    yield word.strip()


def get_line_n_chars_long(
    words_generator: Generator[str, None, None], n_chars: int = 50
) -> Generator[str, None, None]:
    if n_chars < 40:
        raise ValueError("n_chars must be greater than 40.")
    else:
        line: str = ""
        word: str = ""
        to_return: str = ""
        try:
            while True:
                word = next(words_generator)
                if word == "\n":
                    to_return = line.rstrip() + "\n"
                    line = ""
                    yield to_return
                elif len(word) + len(line) <= n_chars:
                    line += word + " "
                else:
                    to_return = line.rstrip()
                    line = word + " "
                    yield to_return
        except StopIteration:
            yield line.lstrip()


def main() -> None:
    LINE_LEN: int = 50
    terminate_program: bool = not are_argv_ok_print_messages_and_get_decision(sys.argv)
    if terminate_program:
        print("Nothing to do. Terminating program.")
    else:
        print("Reading words from file '{0}'".format(sys.argv[1]))
        print("Formatting text to be <= {0} chars per line".format(LINE_LEN))
        print("Printing result.\n")
        for line in get_line_n_chars_long(get_words(sys.argv[1]), LINE_LEN):
            print(line)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
