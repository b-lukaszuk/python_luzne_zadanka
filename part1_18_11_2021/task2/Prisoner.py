import random


class Prisoner:
    """
    Prisoner with a prisoner number [id (incl-incl): 0-99]
    """

    def __init__(self, id: int):
        if 0 <= id <= 99:
            self.__id: int = id
            self.__luckyCardFound: bool = False
        else:
            raise IndexError("Id must be between 0 (incl) and 99 (incl)")

    def getId(self) -> int:
        return self.__id

    def getRandInt(self, fromIncl: int = 0, toIncl: int = 99) -> int:
        return random.randint(fromIncl, toIncl)
