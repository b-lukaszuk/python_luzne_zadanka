from typing import List
import random


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def shuffle_lines_of_text_and_write_to_file(
    file_path: str, contents: List[str]
) -> None:
    random.seed(a=None)
    random.shuffle(contents)
    with open(file_path, "w") as f:
        for line_of_text in contents:
            f.write(line_of_text)


# def main() -> None:
#     for i in range(1880, 1931):
#         print("Reading contents of '{0}'".format("yob" + str(i) + ".csv"))
#         file_contents: List[str] = get_file_contents("./yob" + str(i) + ".csv")
#         print("Shuffling rows.")
#         print("Writing to '{0}'".format("../names_scrambled/yob" + str(i) + ".csv"))
#         shuffle_lines_of_text_and_write_to_file(
#             "../names_scrambled/yob" + str(i) + ".csv", file_contents
#         )
#         print("Done.")
#     print("\nAll jobs finished.")


# if __name__ == "__main__":
#     main()
