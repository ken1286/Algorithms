#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # find largest value
    # find smallest value TO THE LEFT of largest
    # return largest - smallest
    # find biggest difference
    current_max_profit = None
    for n in range(0, len(prices)):
        for i in range(0, n):
            temp_price = prices[n] - prices[i]
            if current_max_profit is None:
                current_max_profit = temp_price
            elif temp_price > current_max_profit:
                current_max_profit = temp_price
    return current_max_profit
    # TODO: Check for solution with 1 for loop using 2 variables
    # buy_index = 0
    # sell_index = len(prices)-1
    # buy = prices[buy_index]
    # sell = prices[sell_index]

    # while buy_index < sell_index:
    #     if max_profit < n:
    #         sell_index -= 1
    #         sell = prices[sell_index]
    #         max_profit = sell - buy
    #     else:
    #         buy_index += 1
    #         buy = prices[buy_index]
    #         if(sell-buy)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
