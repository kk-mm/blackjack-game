import random
from art import logo
def play_blackjack():
    play_the_game = True
    while play_the_game:
        game_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game_play == 'y':
            print(logo)
            
            cards = [11,2,3,4,5,6,7,8,9,10,10,10]
            player_cards = []
            other_cards = []

            player_cards.append(random.choice(cards))
            player_cards.append(random.choice(cards))

            other_cards.append(random.choice(cards))
            other_cards.append(random.choice(cards))

            total_of_player = player_cards[0] + player_cards[1]
            total_of_other = other_cards[0] + other_cards[1]

            print(f"    Your cards: {player_cards}, current score: {total_of_player}")
            print(f"    Computer's first card: {other_cards[0]}")

            if total_of_player == 21:
                if total_of_other == 21:
                    print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                    print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                    print("Both have BlackJack!")
                    print("Draw!")
                    play_blackjack()
                else:
                    print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                    print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                    print("***BlackJack***")
                    print("You Win!")
                    play_blackjack()
            else:
                ask_next_card = True
                while ask_next_card:
                    get_next_card = input("Type 'y' to get another card, type 'n' to pass: ")
                    if get_next_card == 'n':
                        ask_next_card = False
                        ##call_computer_function()
                        if total_of_other == 21:
                            print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                            print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                            print("Computer have BlackJack!")
                            print("You Lose!")
                            play_blackjack()
                        else:
                            pick_new_card = True
                            while pick_new_card:
                                new_card = random.choice(cards)
                                other_cards.append(new_card)
                                total_of_other += new_card
                                if total_of_other > 21 and new_card == 11:
                                    total_of_other -= 10
                                if total_of_other >= 17:
                                    pick_new_card = False
                                    if total_of_other > 21:
                                        print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                                        print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                                        print("Computer went over. You Win!")
                                        play_blackjack()
                                    else:
                                        #Check Result
                                        play_the_game = False
                                        if total_of_player == total_of_other:
                                            print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                                            print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                                            print("Draw!")
                                            play_blackjack()
                                        elif total_of_player > total_of_other:
                                            print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                                            print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                                            print("You Win!")
                                            play_blackjack()
                                        else:
                                            print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                                            print(f"Computer final hand: {other_cards}, final score: {total_of_other}")
                                            print("You Lose!") 
                                            play_blackjack()                               

                    else:
                        new_card = random.choice(cards)
                        player_cards.append(new_card)
                        total_of_player += new_card
                        if total_of_player > 21 and new_card == 11:
                            total_of_player -= 10
                        print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                        print(f"Computer final hand: {other_cards[0]}, final score: {other_cards[0]}")
                        if total_of_player > 21:
                            ask_next_card = False
                            print(f"Your final hand: {player_cards}, final score: {total_of_player}")
                            print(f"Computer final hand: {other_cards[0]}, final score: {other_cards[0]}")
                            print("You went over. You Lose!")
                            play_blackjack()
        else:
            play_blackjack()

play_blackjack()