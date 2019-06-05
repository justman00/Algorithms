#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    # find the min and the max
    # make sure that the min is before the max
    # return their difference
    # if the max is before the min call the function again with a different array
    maximum = max(prices)
    minimum = min(prices)

    maxIndex = prices.index(maximum)
    minIndex = prices.index(minimum)

    if len(prices) == 2:
        return minimum - maximum

    if minIndex < maxIndex:
        return maximum - minimum
    elif minIndex == len(prices) - 1:
        return find_max_profit(prices[:minIndex])
    else:
        return find_max_profit(prices[maxIndex+1:])


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
