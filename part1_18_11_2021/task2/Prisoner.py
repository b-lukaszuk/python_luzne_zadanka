import random


class Prisoner:
    """
    Prisoner - class required by the task
    """

    def __init__(self, id: int):
        self.__id: int = id
        self.__luckyCardFound: bool = False

    def getId(self) -> int:
        return self.__id

    def getRandInt(self, fromIncl: int = 0, toIncl: int = 99) -> int:
        return random.randint(fromIncl, toIncl)

    def isLuckyCardFound(self) -> bool:
        return self.__luckyCardFound

    def setLuckyCardFound(self, setTo: bool) -> None:
        self.__luckyCardFound == setTo
