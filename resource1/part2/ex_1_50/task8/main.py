#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Point import Point
from Circle import Circle
from typing import Callable, List, Tuple


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines details of circle geometry.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")


def print_examples(examples: List[Tuple[Circle, Circle]],
                   expected_answers: List[bool],
                   main_msg: str,
                   every_turn_msg_fn: Callable[[Circle, Circle], str],
                   every_turn_action_fn: Callable[[Circle, Circle], str]
                   ) -> None:
    if len(examples) != len(expected_answers):
        raise ValueError("len(examples) must be equal to len(expected_answers)")
    print(main_msg)
    for i in range(len(examples)):
        circ1, circ2 = examples[i]
        print("-" * 3)
        print(every_turn_msg_fn(circ1, circ2))
        print("Computed answer: {0}".format(every_turn_action_fn(circ1, circ2)))
        print("Expected answer: {0}".format(expected_answers[i]))


def print_examples1() -> None:
    circles1: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(6, 7), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(9, 3), 1)),
        (Circle(Point(6, 7), 1), Circle(Point(7, 6), 4))
    ]
    expected_answers1: List[bool] = [True, False, False]
    print_examples(
        circles1, expected_answers1,
        "\nCircle inside circle examples.",
        lambda c1, c2: "Is {0} completely inside {1}?".format(c2, c1),
        lambda c1, c2: str(c1.is_other_circle_completely_in_me(c2)))


def print_examples2() -> None:
    circles2: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(9, 8), 2)),
        (Circle(Point(7, 6), 4), Circle(Point(6, 7), 1)),
    ]
    expected_answers2: List[bool] = [True, False]
    print_examples(
        circles2, expected_answers2,
        "\nCircles circumferences intersecion examples.",
        lambda c1, c2: "Do ciurcumferences of {0} and {1} intersect?".format(c1, c2),
        lambda c1, c2: str(c1.do_circumferences_intersect(c2)))

def print_examples3() -> None:
    circles3: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(9, 8), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(3, 2), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(4, 10), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(5, 10), 1)),
    ]
    expected_answers3: List[bool] = [True, False, False, True]
    print_examples(
        circles3, expected_answers3,
        "\nCircles overlap examples.",
        lambda c1, c2: "Do circle {0} and {1} overlap?".format(c1, c2),
        lambda c1, c2: str(c1.does_it_overlap(c2)))

def print_examples4() -> None:
    circles4: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(9, 8), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(13, 6), 2)),
    ]
    expected_answers4: List[bool] = [False, True]
    print_examples(
        circles4, expected_answers4,
        "\nCircles touch in 1 point examples.",
        lambda c1, c2: "Do circumferences of {0} and {1} touch in 1 point?".format(c1, c2),
        lambda c1, c2: str(c1.do_circumferences_touch_in_1_point(c2)))


def main() -> None:
    print_program_description()
    print_examples1()
    print_examples2()
    print_examples3()
    print_examples4()
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
