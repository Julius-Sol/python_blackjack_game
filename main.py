############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import sys
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
      


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card():
    return cards[random.randint(0,12)]

def print_hands(player_hand, computers_hand):
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computers_hand[0]}")

def final(player_hand, computers_hand):
    while sum(computers_hand) < 17:
        computers_hand.append(add_card())
    print(f"Your Final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Computer's final hand: {computers_hand}, final score: {sum(computers_hand)}")
    if sum(player_hand) > 21:
        print("You went over. You lose 😰")
    elif sum(computers_hand) > 21:
        print("Opponent went over. You win :)")
    else:
        if sum(player_hand) > sum(computers_hand):
            print("You win :)")
        else: 
            print("You Lose :(")

    start_blackjack()

def play_blackjack():
    print(logo)
    player_hand = [add_card(),add_card()]
    computers_hand = [add_card(),add_card()]
    print_hands(player_hand, computers_hand)
    while True:
        if sum(player_hand) > 21:
            final(player_hand, computers_hand)

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_hand.append(add_card())
            if sum(player_hand) > 21:
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
        else:
             final(player_hand, computers_hand)
            
        print_hands(player_hand, computers_hand)

def start_blackjack():
    print("Do to want to play a game of Blackjack? Type 'y' or 'n':" )
    response = input()
    if response == 'y':
        play_blackjack()
    elif response == 'n':
        sys.exit()
    else:
        print("Invlaid choice")
        start_blackjack();    

        
start_blackjack()