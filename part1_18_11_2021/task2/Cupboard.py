import random

from Card import Card


class Cupboard:
    """
    Cupboard with 100 drawers and 1 Card in each drawer
    """

    def __init__(self, noOfDrawersWithCards: int = 100):
        self.__cards: [Card] = [Card(i) for i in range(noOfDrawersWithCards)]
        random.shuffle(self.__cards)
        self.__upIndexIncl: int = len(self.__cards) - 1

    def getCardIdFromDrawer(self, drawerNo: int) -> int:
        if 0 <= drawerNo <= self.__upIndexIncl:
            return self.__cards[drawerNo].getId()
        else:
            raise IndexError(
                "Drawer number must be between 0 (incl) and {} (incl)".format(
                    self.__upIndexIncl
                )
            )
