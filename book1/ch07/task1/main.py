import os.path
import sys
from typing import List


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def write_contents_to_file(file_path: str, contents: List[str]) -> None:
    with open(file_path, "w") as f:
        for i in range(len(contents)):
            f.write("{0}: {1}".format(i + 1, contents[i]))


def are_sys_argv_ok(sys_argv: List[str]) -> bool:
    return (
        len(sys_argv) == 3
        and os.path.isfile(sys_argv[1])
        and (sys_argv[1] != sys.argv[2])
    )


def print_error_msgs_for_sys_argv(sys_argv: List[str]) -> None:
    if len(sys_argv) != 3:
        print("Incorrect number of arguments sent to program.")
    elif not os.path.isfile(sys_argv[1]):
        print("File {0} does not exist.".format(sys_argv[1]))
    elif sys_argv[1] == sys_argv[1]:
        print("Name of input file must be different than the output file.")
    print("Terminating program.")


def main() -> None:
    if not are_sys_argv_ok(sys.argv):
        print_error_msgs_for_sys_argv(sys.argv)
    else:
        print("Reading contents of {0}".format(sys.argv[1]))
        print("Writing contents with line numbers to {0}".format(sys.argv[2]))
        write_contents_to_file(sys.argv[2], get_file_contents(sys.argv[1]))
        print("Done. That's all. Goodbye!")


if __name__ == "__main__":
    main()
