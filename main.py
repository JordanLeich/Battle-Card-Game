#!/usr/bin/python3
# Made by Jordan Leich on 5/5/21
# TODO 1.

# imports
import colors
import random
import end
import time

# Global variables
game_counter = 0
user_cards = []
ai_cards = []
user_wins = 0
ai_wins = 0


def intro():
    global ai_wins, game_counter, user_wins, user_cards
    print(colors.green + 'Welcome to Clash, made by Jordan Leich.\n' + colors.reset)
    time.sleep(.5)
    print(colors.yellow + '''Important things to know!
1. 
2.\n''' + colors.reset)
    time.sleep(.5)
    game()


def game():
    global ai_wins, game_counter, user_wins, user_cards
    user_health, ai_health = 100, 100

    all_cards = (barbarian_rank_1, barbarian_rank_2, barbarian_rank_3, wizard_rank_1, wizard_rank_2, wizard_rank_3,
                 giant_rank_1, giant_rank_2, giant_rank_3)

    while len(user_cards) <= 3:
        all_cards.shuffle()
        time.sleep(1)

        if 1 in user_cards:
            print(colors.green + 'You have a Barbarian Rank 1 Card\n' + colors.reset)
        elif 2 in user_cards:
            print(colors.green + 'You have a Barbarian Rank 2 Card\n' + colors.reset)
        elif 3 in user_cards:
            print(colors.green + 'You have a Barbarian Rank 3 Card\n' + colors.reset)
        elif 4 in user_cards:
            print(colors.green + 'You have a Wizard Rank 1 Card\n' + colors.reset)
        elif 5 in user_cards:
            print(colors.green + 'You have a Wizard Rank 2 Card\n' + colors.reset)
        elif 6 in user_cards:
            print(colors.green + 'You have a Wizard Rank 3 Card\n' + colors.reset)
        elif 7 in user_cards:
            print(colors.green + 'You have a Giant Rank 1 Card\n' + colors.reset)
        elif 8 in user_cards:
            print(colors.green + 'You have a Giant Rank 2 Card\n' + colors.reset)
        elif 9 in user_cards:
            print(colors.green + 'You have a Giant Rank 3 Card\n' + colors.reset)

    print(user_cards)
    time.sleep(1.5)

    while len(ai_cards) != 3:
        ai_cards.append(random.randint(1, 9))
        time.sleep(1)

        if 1 in ai_cards:
            print(colors.red + 'Opponent got a Barbarian Rank 1 Card\n' + colors.reset)
        elif 2 in ai_cards:
            print(colors.red + 'Opponent got a Barbarian Rank 2 Card\n' + colors.reset)
        elif 3 in ai_cards:
            print(colors.red + 'Opponent got a Barbarian Rank 3 Card\n' + colors.reset)
        elif 4 in ai_cards:
            print(colors.red + 'Opponent got a Wizard Rank 1 Card\n' + colors.reset)
        elif 5 in ai_cards:
            print(colors.red + 'Opponent got a Wizard Rank 2 Card\n' + colors.reset)
        elif 6 in ai_cards:
            print(colors.red + 'Opponent got a Wizard Rank 3 Card\n' + colors.reset)
        elif 7 in ai_cards:
            print(colors.red + 'Opponent got a Giant Rank 1 Card\n' + colors.reset)
        elif 8 in ai_cards:
            print(colors.red + 'Opponent got a Giant Rank 2 Card\n' + colors.reset)
        elif 9 in ai_cards:
            print(colors.red + 'Opponent got a Giant Rank 3 Card\n' + colors.reset)

    time.sleep(1.5)

    while user_health > 0 or ai_health > 0:
        print('Your cards are battling your opponents cards...')
        time.sleep(1)


def restart():  # allows the user to restart or end the game
    user_restart = input('Would you like to restart (yes or no): ')
    print()
    time.sleep(1)

    if user_restart.lower() == 'y' or user_restart.lower() == 'yes':
        print(colors.green + 'Restarting the game...' + colors.reset + '\n')
        time.sleep(1)
        intro()

    elif user_restart.lower() == 'n' or user_restart.lower() == 'no':
        end.end()

    else:
        print(colors.red + 'User Input Restart Error Found...' + colors.reset + '\n')
        time.sleep(1)
        restart()


intro()
