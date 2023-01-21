#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Card import Card
from typing import List


class Cards_Deck():
    def __init__(self) -> None:
        self.__deck__: List[Card] = [Card(r, s) for r in range(2, 15) for s in range(4)]

    def __str__(self) -> str:
        return "\n".join([c.__str__() for c in self.__deck__])
