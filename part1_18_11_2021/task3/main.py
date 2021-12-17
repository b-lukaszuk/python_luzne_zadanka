#!/usr/bin/env python3.8
import sys
from Board import Board


def printIntro():
    print("Hello, let's play '15 puzzle game'\n")
    print(
        "Your task is to order the numbers from 1 to 15 (empty goes after 15)"
    )
    print("You can move one field at a time")
    print("The field must be a neighbour to the empty field\n")
    print("The game will end automatically one the puzzle is solved\n")
    print("To leave in the middle of the game press Ctrl+c\n")
    print("All clear? OK. Let's begin :)")


def main():
    b: Board = Board()
    printIntro()
    while not b.isBoardSolved():
        print()  # newline
        print(b)
        print("Enter Your move: 1-15: ")
        try:
            userChoice: int = int(input())
            if not b.isMoveLegal(userChoice):
                print("That's an illegal move try again.")
            else:
                b.makeMove(userChoice)
                print("Move made")
        except ValueError:
            print("That was not a number")
        except KeyboardInterrupt:
            print("\nYou want to leave? OK. See You next time. Goodbye!")
            sys.exit()
    print("\nThat's it. The puzzle is solved. You won. Congratulations!")
    print("Behold the solved puzzle:")
    print(b)
    print("\nOK. The game is finished. Goodbye!")


if __name__ == "__main__":
    main()
