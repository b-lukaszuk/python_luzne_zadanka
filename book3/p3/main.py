#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Card import Card
from Cards_Deck import Cards_Deck
from Hand import Hand
from typing import List, Tuple


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


def deal_cards(cards: Cards_Deck) -> Tuple[Hand, Hand]:
    """deals hand of cards for dealer and player
    modifies cards (removes some random cards from it)"""
    dealer_hand, player_hand = Hand(), Hand()
    dealer_hand.add_card(cards.get_rand_card(), cards.get_rand_card())
    dealer_hand.cover_first_card()
    player_hand.add_card(cards.get_rand_card(), cards.get_rand_card())
    return dealer_hand, player_hand


def get_player_decision() -> str:
    decision: str = ""
    while not (decision == "h" or decision == "s"):
        print("What You want to do?")
        print("Press h to Hit, i.e. take another card")
        print("Press s to Stand, i.e. stop taking cards")
        decision = input("Your decision: ")
    return decision


def declare_hands(dealer_hand: Hand, player_hand: Hand, print_hand_value: bool) -> None:
    msg1: str = f"Dealer cards: {dealer_hand}" + (
        f" , value: {dealer_hand.get_value()}" if print_hand_value else ""
    )
    msg2: str = f"Player cards: {player_hand}" + (
        f" , value: {player_hand.get_value()}" if print_hand_value else ""
    )
    print("---")
    print(msg1, msg2, sep="\n")
    print("---")


def declare_winner(dealer_hand: Hand, player_hand: Hand) -> None:
    if dealer_hand.is_busted() and player_hand.is_busted():
        print("Both dealer and player busted. Draw.")
    elif dealer_hand.is_busted():
        print("Dealer busted. Player wins.")
    elif player_hand.is_busted():
        print("Player busted. Dealer wins.")
    elif dealer_hand.get_value() > player_hand.get_value():
        print("Dealer wins.")
    elif dealer_hand.get_value() < player_hand.get_value():
        print("Player wins.")
    else:
        print("Draw.")


def main() -> None:
    print_game_description()
    cards: Cards_Deck = Cards_Deck()
    dealer_hand, player_hand = deal_cards(cards)
    declare_hands(dealer_hand, player_hand, False)
    decision: str = get_player_decision()
    if decision == "h":
        player_hand.add_card(cards.get_rand_card())
    print("---")
    print("Gentelmen show cards")
    dealer_hand.uncover_all_cards()
    declare_hands(dealer_hand, player_hand, True)
    declare_winner(dealer_hand, player_hand)
    print("---")
    print("\nPROGRAM STATUS: TO BE FINISHED.")
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
