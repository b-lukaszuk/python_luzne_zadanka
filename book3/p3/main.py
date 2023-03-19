#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Card import Card
from Cards_Deck import Cards_Deck
from Hand import Hand
from typing import List, Tuple


def get_rules_description() -> str:
    lines_of_text: List[str] = [
        "RULES OF THE CARD GAME",
        "----------------------",
        "At the beginning the dealer and the player are dealt 2 cards each.",
        "One of the dealer cards is covered.",
        "The goal is to get as close to 21 without going over.",
        "Kings, Queens, and Jacks are worth 10 points.",
        "Aces are worth 1 or 11 points.",
        "Cards 2 through 10 are worth their face value.",
        "----------------------------\n",
    ]
    return "\n".join(lines_of_text)


def get_actions_description() -> str:
    lines_of_text: List[str] = [
        "ACTIONS",
        "-------",
        "The player goes first. The dealer second.",
        "Options are:",
        "(H)it to take another card.",
        "(S)tand to stop taking cards.",
        "On your first play, you can (D)ouble down to increase your bet",
        "but must hit exactly one more time before standing.",
        "The dealer stops hitting at 17.",
        "----------------------------\n",
    ]
    return "\n".join(lines_of_text)


def get_end_of_round_description() -> str:
    lines_of_text: List[str] = [
        "END OF ROUND",
        "------------",
        "The round ends: when both player and dealer stop hitting or one of them busts.",
        "The player with a higher hand (but not greater than 21) wins.",
        "In case of a tie, the bet is returned to the player.",
        "----------------------------\n",
    ]
    return "\n".join(lines_of_text)


def print_game_description() -> None:
    print("Welcome to the game of Blackjack\n")
    print(get_rules_description())
    print(get_actions_description())
    print(get_end_of_round_description())
    print("All Crear! Then let's begin!")
    _ = input("Press Enter to continue.")
    print()


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
    while decision not in ["h", "s"]:
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
    print("---\n")


# it modifies player-hand if player chooses to hit
def run_player_hit_loop(player_hand: Hand, cards: Cards_Deck) -> None:
    """allows player to hit until he chooses stay or busts.
    if player chooses hit, it modifies player_hand and cards,
    it adds a card to hand"""
    print("--ON MOVE: PLAYER--")
    decision: str = "h"
    while (not player_hand.is_busted()) and decision == "h":
        print(f"\nPlayer cards: {player_hand}, value: {player_hand.get_value()}")
        decision = get_player_decision()
        if decision == "h":
            player_hand.add_card(cards.get_rand_card())
    print("--PLAYER'S MOVE FINISHED--")


def run_dealer_hit_loop(dealer_hand: Hand, cards: Cards_Deck) -> None:
    """allows dealer to hit until he reaches 17 or busts.
    it modifies dealer_hand and cards, it adds a card to hand"""
    print("\n--ON MOVE: DEALER--")
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(cards.get_rand_card())
    dealer_hand.uncover_all_cards()
    print(f"Dealer cards: {dealer_hand}, value: {dealer_hand.get_value()}")
    print("--DEALER'S MOVE FINISHED--\n")


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


def print_competitors_cards(
    dealer_hand: Hand, player_hand: Hand, print_values: bool = False
) -> None:
    print(
        f"Dealer cards: {dealer_hand}"
        + (f", value: {dealer_hand.get_value()}" if print_values else "")
    )
    print(
        f"Player cards: {player_hand}"
        + (f", value: {player_hand.get_value()}" if print_values else "")
    )


def main() -> None:
    print_game_description()
    cards: Cards_Deck = Cards_Deck()
    dealer_hand, player_hand = deal_cards(cards)
    declare_hands(dealer_hand, player_hand, False)
    run_player_hit_loop(player_hand, cards)
    if player_hand.is_busted():
        dealer_hand.uncover_all_cards()
    else:
        run_dealer_hit_loop(dealer_hand, cards)

    print("---")
    print("Game Over.")
    declare_hands(dealer_hand, player_hand, True)
    declare_winner(dealer_hand, player_hand)
    print("---")
    print("\nPROGRAM STATUS: TO BE FINISHED.")
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
