import random
from Card import Card


class Cupboard:
    """
    Cupboard with 100 drawers and 1 Card in each drawer
    """

    def __init__(self):
        self.__cards: [Card] = [Card(i) for i in range(99)]
        random.shuffle(self.__cards)

    def getCardIdFromDrawer(self, drawerNo: int) -> int:
        if 0 <= drawerNo <= 99:
            return self.__cards[drawerNo].getId()
        else:
            raise IndexError(
                "Drawer number must be between 0 (incl) and 99 (incl)"
            )
