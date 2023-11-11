import random

def create_deck():
    nbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Coeur', 'Carreau', 'Treffles', 'Pic']
    return [{'nb': nb, 'suit': suit} for nb in nbs for suit in suits]

def play_game():
    deck = create_deck()
    random.shuffle(deck)

    selected_card = random.choice(deck)

    nb_card = selected_card['nb']
    nb_search = 0
    while deck[nb_search]['nb'] != nb_card:
        nb_search += 1

    return nb_search

def main():
    nb_simulations = 1000
    total_nb_search = 0

    for _ in range(nb_simulations):
        total_nb_search += play_game()

    mean = total_nb_search / nb_simulations
    print("La moyenne pour ", nb_simulations, " simulations est de ", mean)

if __name__ == "__main__":
    main()
