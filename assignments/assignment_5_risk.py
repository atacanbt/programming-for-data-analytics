# This program simulates 1000 rounds of Risk (boardgame) battles and plots the result.
# The program uses the numpy and matplotlib libraries.
# Author: Atacan Buyuktalas

import numpy as np
import matplotlib.pyplot as plt

# Rolling the dice
def roll_dice(num_dice):
    # negating the array to sort in descending order
    return -np.sort(-np.random.randint(1,7, size = num_dice))


# Simulating a battle between two armies
def single_battle():
    attacker_rolls = roll_dice(3)
    defender_rolls = roll_dice(2)
    # comparing the highest dice rolls of both sides
    num_comparison = min(len(attacker_rolls), len(defender_rolls))
    attacker_best = attacker_rolls[:num_comparison]
    defender_best = defender_rolls[:num_comparison]
    # counting the losses
    attacker_losses = np.sum(attacker_best <= defender_best)
    defender_losses = np.sum(attacker_best > defender_best)

    return attacker_losses, defender_losses

def multiple_battles(num_rounds):
    attacker_wins = 0
    defender_wins = 0
    # simulating the specific number of rounds
    for _ in range(num_rounds):
        attacker_losses, defender_losses = single_battle()
        if attacker_losses < defender_losses:
            attacker_wins += 1
        else:  # In case of a tie, defender wins
            defender_wins += 1
    return attacker_wins, defender_wins

# Plotting the results of the full war
def war():
    num_rounds = 1000
    attacker_wins, defender_wins = multiple_battles(num_rounds)

    labels = ['Attacker Wins', 'Defender Wins']
    counts = [attacker_wins, defender_wins]

    bars = plt.bar(labels, counts, color = ['red', 'blue'])
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, str(height), 
                 ha = 'center', va = 'bottom', fontsize = 12)

    plt.title(f'Results of {num_rounds} rounds of Risk battles')
    plt.ylabel('Number of wins')
    plt.show()

if __name__ == '__main__':
    war()