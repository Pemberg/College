import random
import sys

def main():
    # Initialize the deck of cards
    deck = []
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    colors = ["Clubs", "Diamonds", "Hearts", "Spades"]

    for color in colors:
        for value in values:
            deck.append(str(value) + ' ' + color)
    random.shuffle(deck)

    # Divide the deck between two players
    player1_deck = deck[:len(deck) // 2]
    player2_deck = deck[len(deck) // 2:]

    max_rounds = 1000  # maximum number of rounds

    round_num = 1
    try:
        player1_wins = 0
        player2_wins = 0

        # Start the game loop
        while player1_deck and player2_deck:
            print('Round', round_num)
            print('Player 1:', player1_deck[0])
            print('Player 2:', player2_deck[0])

            # Compare card values and assign points
            player1_card = int(player1_deck[0].split()[0])
            player2_card = int(player2_deck[0].split()[0])

            if player1_card > player2_card:
                print('Player 1 wins this round!')
                player1_deck.append(player1_deck.pop(0))
                player1_deck.append(player2_deck.pop(0))
                player1_wins += 1
            elif player1_card < player2_card:
                print('Player 2 wins this round!')
                player2_deck.append(player2_deck.pop(0))
                player2_deck.append(player1_deck.pop(0))
                player2_wins += 1
            else:
                print('Draw!')
                player1_deck.append(player1_deck.pop(0))
                player2_deck.append(player2_deck.pop(0))

            round_num += 1

            if round_num > max_rounds:
                force_game_end(player1_wins, player2_wins)
                break

        # Announce the winner
        if player1_deck:
            print('\nPLAYER 1 WINS THE GAME!')
        elif player2_deck:
            print('\nPLAYER 2 WINS THE GAME!')
        else:
            print('\nDRAW!')

    except KeyboardInterrupt:
        print("\nGame interrupted.")
        sys.exit()

def force_game_end(player1_wins, player2_wins):
    # Function to end the game if the maximum number of rounds is reached
    print("\nMaximum number of rounds reached. Game ends.")

main()
