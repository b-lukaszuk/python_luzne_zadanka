from typing import Dict, List, TypedDict


class Elements(TypedDict):
    fullNames: List[str]
    symbols: List[str]
    atomicNumbers: List[str]


def get_file_contents(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
    return lines


def add_values_to_elements(elements: Elements, line_from_csv: List[str]) -> None:
    elements["fullNames"].append(line_from_csv[2].strip())
    elements["symbols"].append(line_from_csv[1].strip())
    elements["atomicNumbers"].append(line_from_csv[0].strip())


def get_elements_from_file(
    file_path: str = "./PubChemElements_all.csv",
) -> Elements:
    elements: Elements = {"fullNames": [], "symbols": [], "atomicNumbers": []}
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
    result: str = ""
    for key in ["fullNames", "symbols", "atomicNumbers"]:
        result += "{0}: {1}, ".format(key[:-1], elements[key][elt_position])
    return result[:-2]


def ask_user_for_action() -> str:
    input_collected: bool = False
    user_choice: str = ""
    keysDict: Dict = {"f": "fullNames", "s": "symbols", "a": "atomicNumbers"}
    msg: str = "Action types:\n"
    msg += "\ttype 'f': chose element by full name\n"
    msg += "\ttype 's': chose element by symbol\n"
    msg += "\ttype 'a': chose element by atomic number (# of protons)\n"
    while not input_collected:
        print(msg)
        user_choice = input("Enter Your choice: ")
        if user_choice.strip().lower() not in keysDict:
            print("Incorrect input. Try again.\n")
        else:
            input_collected = True
    return keysDict[user_choice.strip().lower()]


def ask_user_for_search_phrase(key_from_elements: str) -> str:
    keysDict: Dict = {
        "fullNames": "full name",
        "symbols": "symbol",
        "atomicNumbers": "atomic number (# of protons)",
    }
    searched_phrase: str = input(
        "Type {0} of the searched element: ".format(keysDict[key_from_elements])
    )
    return searched_phrase.strip()


def main() -> None:
    print("Done. That's all. Goodbye!")


if __name__ == "__main__":
    main()
