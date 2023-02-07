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

    def add_card(self, *cards: Card) -> None:
        self.__cards__.extend(cards)

    def get_value(self) -> int:
        sum1, sum2 = (0, 0)
        for (v1, v2) in [c.get_value() for c in self.__cards__]:
            sum1 += v1
            sum2 += v2
        if max(sum1, sum2) < 22:
            return max(sum1, sum2)
        else:
            return min(sum1, sum2)

    def is_busted(self) -> bool:
        return self.get_value() > 21

    def cover_first_card(self) -> None:
        if not self.__cards__[0].is_covered():
            self.__cards__[0].toggle_covered()

    def uncover_all_cards(self) -> None:
        for card in self.__cards__:
            if card.is_covered():
                card.toggle_covered()
