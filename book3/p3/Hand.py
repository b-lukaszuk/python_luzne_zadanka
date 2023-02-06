#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Card import Card
from typing import List


class Hand:
    def __init__(self) -> None:
        self.__cards__: List[Card] = []

    def __str__(self) -> str:
        if self.__cards__:
            return ", ".join([c.__str__() for c in self.__cards__])
        else:
            return "The hand is empty"

    def add_card(self, card: Card) -> None:
        self.__cards__.append(card)

    def get_value(self) -> int:
        sum1, sum2 = (0, 0)
        for (v1, v2) in [c.get_value() for c in self.__cards__]:
            sum1 += v1
            sum2 += v2
        if max(sum1, sum2) < 22:
            return max(sum1, sum2)
        else:
            return min(sum1, sum2)