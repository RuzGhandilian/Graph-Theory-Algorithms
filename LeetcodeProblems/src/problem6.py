# Problem 6: Best Time to Buy and Sell Stock II

def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # if price goes up, we buy and sell
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
