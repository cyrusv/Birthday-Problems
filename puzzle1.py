# Monte Carlo Simulation

# Puzzle 1
# If I simultaneously roll 50 die, what is the probability that
# the sum of all the faces will be either a multiple of 3 or a number whose last digit is 7?
# Round to the nearest percent.

from __future__ import division
import random

def monte_carlo(simulations):
    """
    Returns a list of sums after running X number of simulations of rolling 50 die.
    """
    list_of_sums = []

    for i in range(simulations):
        sum = 0
        for j in range(50):
            sum += random.randint(1, 6)
        list_of_sums.append(sum)

    return list_of_sums

def find_probability(list_of_sums):
    """
    Returns the probability that a sum in the list of sums
    is either a multiple of 3 or whose last digit is 7
    """
    count = 0

    for sum in list_of_sums:
        if sum % 3 == 0 or sum % 10 == 7:
            count += 1

    prob = count/len(list_of_sums)

    print 'The probability that the sum is either a multiple of 3 or whose last digit is 7 is:'
    print round(prob, 3)

find_probability(monte_carlo(10))

import pdb
pdb.set_trace()