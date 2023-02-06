#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Card import Card
from Cards_Deck import Cards_Deck
from Hand import Hand
from typing import List


def print_game_description() -> None:
    print("Welcome to the game of Blackjack")
    print("Rules")
    print("Try to get as close to 21 without going over.")
    print("Kings, Queens, and Jacks are worth 10 points.")
    print("Aces are worth 1 or 11 points.")
    print("Cards 2 through 10 are worth their face value.")
    print("(H)it to take another card.")
    print("(S)tand to stop taking cards.")
    print("On your first play, you can (D)ouble down to increase your bet")
    print("but must hit exactly one more time before standing.")
    print("In case of a tie, the bet is returned to the player.")
    print("The dealer stops hitting at 17.")
    _ = input("Press Enter to continue.")


def main() -> None:
    print_game_description()
    cards: Cards_Deck = Cards_Deck()
    h1: Hand = Hand()
    h2: Hand = Hand()
    print(h1)
    print(h2)
    h1.add_card(cards.get_rand_card())
    h1.add_card(cards.get_rand_card())
    h2.add_card(cards.get_rand_card())
    h2.add_card(cards.get_rand_card())
    print(f"{h1}, value {h1.get_value()}")
    print(f"{h2}, value {h2.get_value()}")
    print("\nPROGRAM STATUS: TO BE FINISHED.")
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
    print("\nPROGRAM STATUS: TO BE FINISHED.")
    print("\nThat's all. Goodbye!")