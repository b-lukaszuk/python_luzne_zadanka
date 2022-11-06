from typing import List, Set, TypedDict


class Names(TypedDict):
    M: Set[str]
    F: Set[str]


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def extract_names(file_contents: List[str]) -> Names:
    names: Names = {"M": set(), "F": set()}
    name: str = ""
    gender: str = ""
    for line in file_contents:
        name, gender, _ = line.split(",")
        names[gender].add(name)
    return names


def get_union_of_names1_and_names2(names1: Names, names2: Names) -> Names:
    all_names: Names = {"M": set(), "F": set()}
    for key in ["M", "F"]:
        all_names[key] = names1[key].union(names2[key])
    return all_names


def print_program_description() -> None:
    print("\nHi. This is a toy program that reads CSV files.")
    print("The files are located at './datasets/'.")
    print("The files are named: 'yob{1880..1889}.csv'.")
    print("They were downloaded from public source, i.e.")
    print("https://www.ssa.gov/oact/babynames/limits.html")
    print("The program reads every file.")
    print("Next it determines unique names that occur in files.")
    print("The result is printed to the screen.")
    print("Unique names are determined for each gender separately.")
    print("Only 5 female and 5 male names from each file will be taken.")
    print("This should increase the readability of the output.")
    print("NO GUARANTEE OF THE PROGRAM ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")
    _: str = input("Press any key to begin ")


def read_all_files_print_unique_names() -> None:
    path_to_folder_with_datafiles: str = "./datasets/"
    full_path: str = path_to_folder_with_datafiles
    file_contents: List[str] = []
    unique_names: Names = {"M": set(), "F": set()}
    for year in range(1880, 1890):
        full_path: str = path_to_folder_with_datafiles + "yob" + str(year) + ".csv"
        print("\nReading file {0}".format(full_path))
        file_contents = get_file_contents(full_path)
        print("Taking first 5 female and last 5 male names from the file.")
        print("Adding them to the list of unique names.")
        unique_names = get_union_of_names1_and_names2(
            unique_names, extract_names(file_contents[:5] + file_contents[-5:])
        )
    print("\nAll done.")
    print("\nUnique names: {0}".format(unique_names))


def main() -> None:
    print_program_description()
    read_all_files_print_unique_names()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
