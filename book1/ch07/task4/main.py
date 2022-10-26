import os.path
import re
import sys
from typing import List


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def write_contents_to_file(file_path: str, contents: List[str]) -> None:
    with open(file_path, "w") as f:
        [f.write(line) for line in contents]


def remove_comments(contents: List[str]) -> List[str]:
    return [re.sub(r"#.*", "", line) for line in contents]


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
        print("File '{0}' does not exist.".format(sys_argv[1]))
    elif sys_argv[1] == sys_argv[1]:
        print("Name of input file must be different than the output file.")
    print("Terminating program.")


def main() -> None:
    if not are_sys_argv_ok(sys.argv):
        print_error_msgs_for_sys_argv(sys.argv)
    else:
        print("Reading contents of '{0}'".format(sys.argv[1]))
        contents: List[str] = get_file_contents(sys.argv[1])
        print("Removing comments.")
        contents = remove_comments(contents)
        print("Writing contents without comments to '{0}'".format(sys.argv[2]))
        write_contents_to_file(sys.argv[2], contents)
        print("Done. That's all. Goodbye!")


if __name__ == "__main__":
    main()
