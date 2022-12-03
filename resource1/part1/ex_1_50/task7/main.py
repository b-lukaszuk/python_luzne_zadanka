# -*- coding: utf-8 -*-


def main() -> None:
    print("Printing text without new lines and spaces.")
    print("Examples:\n")

    print("Example", "1", ":", "Hello", "there", "!", sep="", end="")
    print("Example", "2", ":", "General", "Kenobi", ".", sep="", end="")

    print("\n\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
