
import random
from art import logo
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):

    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1) 

    return sum(cards)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "            It's a draw"
    elif computer_score == 0:
        return "            You lose. Computer has blackjack"
    elif user_score == 0:
        return "            You win"
    elif user_score > 21:
        return "            You lose, you went over 21"
    elif computer_score > 21:
        return "            You win. Computer went over 21"
    elif user_score > computer_score:
        return "            You win"
    else:
        return "            You lose"


def play_game():
    user_cards = []
    computer_cards = []

    game_over = False
    print(logo)
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while game_over != True:
      print(f"             Your cards {user_cards} with a score of: {user_score}")
      print(f"             Computer's first card {computer_cards[0]}")
      
      if computer_score == 0 or user_score == 0 or user_score > 21:
        game_over = True       

      else:
          draw_another_card = input("Do you want to draw another card? Type 'Yes' or 'No': ").lower()
          if draw_another_card == "yes":
            user_cards.append(deal_card())

            user_score = calculate_score(user_cards)
          else:
            game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)       

    print(compare(user_score, computer_score))
    print(f"             Your cards {user_cards} with a score of: {user_score}")
    print(f"             Computer's cards {computer_cards} and total: {computer_score}")    
    
restart_game = input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").lower()
if restart_game == "yes":
    os.system('clear')
    play_game()