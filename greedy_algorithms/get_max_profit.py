def get_max_profit(stock_prices):
    # initialize the lowest_price to the first stock price
    lowest_price = stock_prices[0]
    # initialize the max_profit to the
    # difference between the first and the second stock price
    max_profit = stock_prices[1] - stock_prices[0]
    # loop through every price in stock_prices
    # starting from the second price
    for index in range(1, len(stock_prices)):
        # if price minus lowest_price is greater than max_profit
        if stock_prices[index] - lowest_price > max_profit:
            # set max_profit to the difference between price and lowest_price
            max_profit = stock_prices[index] - lowest_price
        # if price is lower than lowest_price
        if stock_prices[index] < lowest_price:
            # set lowest_price to price
            lowest_price = stock_prices[index]
    # return max_profit
    return max_profit
