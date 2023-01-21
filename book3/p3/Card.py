#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Dict


class Card():
    # rank 2-10, 11-14 for: J, Q, K, A
    # suit: 0-3 for: clubs, diamonds, hearts, spades
    def __init__(self, rank: int, suit: int) -> None:
        if 2 <= rank <= 14:
            raise ValueError("The rank must be in range(2, 15)")
        if 0 <= suit <= 3:
            raise ValueError("The suit must be in range(4)")
        self.__rank__: int = rank
        self.__suit__: int = suit

    def __get_rank_representation__(self) -> str:
        court_cards: Dict[int, str] = {11: "J", 12: "Q", 13: "K", 14: "A"}
        if self.__rank__ < 11:
            return str(self.__rank__)
        else:
            return court_cards[self.__rank__]

    def __get_suit_representation__(self) -> str:
        suits_symbols: Dict[int, str] = {0: "\u2663", 1: "\u2662", 2: "\u2661", 3: "\u2660"}
        return suits_symbols[self.__suit__]

    def __str__(self) -> str:
        return "{0}{1}".format(
            self.__get_rank_representation__(),
            self.__get_suit_representation__())

    def __repr__(self) -> str:
        return self.__str__()
