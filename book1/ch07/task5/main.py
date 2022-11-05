from typing import Dict, List, TypedDict


class Elements(TypedDict):
    full_names: List[str]
    symbols: List[str]
    atomic_numbers: List[str]
    atomic_masses: List[str]


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def add_values_to_elements(elements: Elements, line_from_csv: List[str]) -> None:
    elements_keys_to_columns: Dict[str, int] = {
        "full_names": 2,
        "symbols": 1,
        "atomic_numbers": 0,
        "atomic_masses": 3,
    }
    for key in elements_keys_to_columns:
        elements[key].append(line_from_csv[elements_keys_to_columns[key]].strip())


def get_elements_from_file(file_path: str) -> Elements:
    elements: Elements = {
        "full_names": [],
        "symbols": [],
        "atomic_numbers": [],
        "atomic_masses": [],
    }
    lines: List[str] = get_file_contents(file_path)
    for i in range(1, len(lines)):
        # fields are separated with commas, and fields contain quotations
        splitted_line: List[str] = lines[i].replace('"', "").split(",")
        add_values_to_elements(elements, splitted_line)
    return elements


def get_element_position(searched_phrase: str, key: str, elements: Elements) -> int:
    position: int = -99
    try:
        position = elements[key].index(searched_phrase)
    except ValueError:
        position = -1
    except KeyError:
        position = -99
    return position


def get_element_description(elt_position: int, elements: Elements) -> str:
    if elt_position < 0:
        return "Element not found"
    elements_keys_to_descriptions: Dict[str, str] = {
        "full_names": "full name",
        "symbols": "symbol",
        "atomic_numbers": "atomic number (# of protons)",
        "atomic_masses": "atomic mass",
    }
    result: str = ""
    for key in ["full_names", "symbols", "atomic_numbers", "atomic_masses"]:
        result += "{0}: {1}, ".format(
            elements_keys_to_descriptions[key], elements[key][elt_position]
        )
    return result[:-2]


def ask_user_for_action() -> str:
    input_collected: bool = False
    user_choice: str = ""
    user_choice_to_elts_key: Dict[str, str] = {
        "f": "full_names",
        "s": "symbols",
        "a": "atomic_numbers",
    }
    msg: str = "\nAvailable action types:\n"
    msg += "\ttype 'f': chose element by full name\n"
    msg += "\ttype 's': chose element by symbol\n"
    msg += "\ttype 'a': chose element by atomic number (# of protons)\n"
    while not input_collected:
        print(msg)
        user_choice = input("Enter Your choice: ")
        if user_choice.strip().lower() not in user_choice_to_elts_key:
            print("Incorrect input. Try again.\n")
        else:
            input_collected = True
    return user_choice_to_elts_key[user_choice.strip().lower()]


def ask_user_for_search_phrase(key_from_elements: str) -> str:
    elements_keys_to_search_phrase: Dict[str, str] = {
        "full_names": "full name",
        "symbols": "symbol",
        "atomic_numbers": "atomic number (# of protons)",
    }
    searched_phrase: str = input(
        "Type {0} of the searched element: ".format(
            elements_keys_to_search_phrase[key_from_elements]
        )
    )
    return searched_phrase.strip()


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program searching through the elements periodic table.")
    print("The table is based on publicly available PubChem data.")
    print("You can search using full name, symbol or atomic number of an element.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF THE PROGRAM ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's start.")
    _: str = input("Press any key to begin ")


def run_main_loop(elements: Elements) -> None:
    end_program: bool = False
    key_from_elts: str = ""
    searched_phrase: str = ""
    elt_position: int = -99
    while not end_program:
        key_from_elts = ask_user_for_action()
        searched_phrase = ask_user_for_search_phrase(key_from_elts)
        elt_position = get_element_position(searched_phrase, key_from_elts, elements)
        print(get_element_description(elt_position, elements))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]


def main() -> None:
    path_to_elements_data: str = "./PubChemElements_all.csv"
    print_program_description()
    print("\nObtaining elements data from {0}".format(path_to_elements_data))
    elements: Elements = get_elements_from_file(path_to_elements_data)
    print("Done.\n\nObtaining user's input.")
    run_main_loop(elements)
    print("\nObtaining user's input completed.")
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
