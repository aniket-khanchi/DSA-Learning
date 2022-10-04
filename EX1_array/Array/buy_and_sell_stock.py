"""
Given an array of numbers consisting of daily stock prices, 
calculate the maximum amount of profit that can be made from 
buying on one day and selling on another.

In an array of prices, each index represents a day, and the value 
on that index represents the price of the stocks on that day.
"""

def buy_and_sell_stock_once(prices):
    max_profit = 0
    min_price = float('inf')
    for i in prices:
        min_price = min(i,min_price)
        compare = i - min_price
        max_profit = max(max_profit,compare)
    return max_profit


print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
