from typing import List, Tuple, TypedDict


class PeopleNames(TypedDict):
    first_names: List[str]
    genders: List[str]
    nums_of_occurences: List[int]


class MostPopularNames(TypedDict):
    female: Tuple[str, int]
    male: Tuple[str, int]


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def file_contents_to_people_names(file_contents: List[str]) -> PeopleNames:
    people_names: PeopleNames = {
        "first_names": [],
        "genders": [],
        "nums_of_occurences": [],
    }
    name: str
    gender: str
    no_of_occurences: str
    # each name occurs only once in a file
    for line in file_contents:
        name, gender, no_of_occurences = line.split(",")
        people_names["first_names"].append(name)
        people_names["genders"].append(gender)
        people_names["nums_of_occurences"].append(int(no_of_occurences))
    return people_names


def print_program_description() -> None:
    print("\nHi. This is a toy program that reads CSV files.")
    print("The files are located at './datasets/names_scrambled/'.")
    print("The files are named: 'yob{1880..1930}.csv'.")
    print("They were downloaded from public source, i.e.")
    print("https://www.ssa.gov/oact/babynames/limits.html")
    print("The program reads every file.")
    print("Next it determines most popular name in a file/year.")
    print("The result is printed to the screen.")
    print("NO GUARANTEE OF THE PROGRAM ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")
    _: str = input("Press any key to begin ")


def people_names_to_most_popular_names(
    people_names: PeopleNames,
) -> MostPopularNames:

    maxMale: int
    maxFemale: int
    maxMale, maxFemale = 0, 0
    result: MostPopularNames = {"female": ("", 0), "male": ("", 0)}

    for i in range(len(people_names["first_names"])):
        if (
            people_names["genders"][i] == "F"
            and people_names["nums_of_occurences"][i] > maxFemale
        ):
            maxFemale = people_names["nums_of_occurences"][i]
            result["female"] = (people_names["first_names"][i], maxFemale)
        if (
            people_names["genders"][i] == "M"
            and people_names["nums_of_occurences"][i] > maxMale
        ):
            maxMale = people_names["nums_of_occurences"][i]
            result["male"] = (people_names["first_names"][i], maxMale)
    return result


def read_all_files_print_most_popular_names() -> None:
    path_to_folder_with_datafiles: str = "./datasets/names_scrambled/"
    full_path: str = path_to_folder_with_datafiles
    most_popular_names: MostPopularNames = {"female": ("", 0), "male": ("", 0)}
    for year in range(1880, 1930):
        full_path: str = path_to_folder_with_datafiles + "yob" + str(year) + ".csv"
        print("\nReading file {0}".format(full_path))
        most_popular_names = people_names_to_most_popular_names(
            file_contents_to_people_names(get_file_contents(full_path))
        )
        print("Most popular names: {0}".format(most_popular_names))


def main() -> None:
    print_program_description()
    read_all_files_print_most_popular_names()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
