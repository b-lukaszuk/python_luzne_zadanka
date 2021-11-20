class Card:
    """
    Card with a number [id (incl-incl): 0-99] written on in it
    """

    def __init__(self, id: int):
        if 0 <= id <= 99:
            self.__id: int = id
        else:
            raise IndexError("Id must be between 0 (incl) and 99 (incl)")

    def getId(self) -> int:
        return self.__id
