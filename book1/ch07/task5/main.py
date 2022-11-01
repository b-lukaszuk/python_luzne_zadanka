from typing import List, TypedDict


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


def main() -> None:
    print("Done. That's all. Goodbye!")


if __name__ == "__main__":
    main()
