# -*- coding: utf-8 -*-

import os
import platform


def main() -> None:
    print("Hi. This program prints basic information about your computer.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("Still, I hope it may be useful. Let's begin.\n")

    print("System name: {0}".format(os.uname().sysname))
    print("Platform name: {0}".format(platform.platform()))
    print("Release: {0}".format(platform.release()))

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
