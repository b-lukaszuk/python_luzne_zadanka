# -*- coding: utf-8 -*-

from typing import List


# https://www.baeldung.com/cs/array-generate-all-permutations#bd-simple-recursive-algorithm
def permutation(
    generated_permutations: List[str],
    next_permutation: str,
    remaining_elements: str,
) -> List[str]:
    if len(remaining_elements) > 0:
        result: List[str] = []
        for elt in remaining_elements:
            next_perm = next_permutation + elt
            rem_elts = remaining_elements.replace(elt, "")
            result = permutation(generated_permutations, next_perm, rem_elts)
        return result
    else:
        generated_permutations.append(next_permutation)
        return generated_permutations


def get_permutations(text: str) -> List[str]:
    if not (1 < len(text) < 7):
        raise ValueError("Length of a string must be between 2 and 7 (incl-incl).")
    return permutation([], "", text)


def main() -> None:
    # not aeiou, since fact(5) = 120, here fact(3) = 6
    tested_str: str = "aei"
    print("Printing all permutations of a string using recursive function.\n")
    print("Tested string '{0}'.".format(tested_str))
    print("Result: {0}".format(get_permutations(tested_str)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
