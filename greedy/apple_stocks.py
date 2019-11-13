def get_max_profit(stock_prices):
    # initialize minimum_stock_price to the first price in stock_prices
    minimum_stock_price = stock_prices[0]
    # initialize max_profit to the difference between first and second prices
    max_profit = stock_prices[1] - stock_prices[0]
    # loop through the stock_prices
    for price in stock_prices:
        # check if the current price is less than minimum_stock_price
        if price < minimum_stock_price:
            # replace minimum_stock_price with current stock
            minimum_stock_price = price
        # initialize current_max_profit to price minus minimum_stock_price
        current_max_profit = price - minimum_stock_price
        # check if the difference between current price and minimum stock
        # price is greater than max_profit
        if current_max_profit > max_profit:
            # replace max_profit with the difference
            max_profit = current_max_profit
    # return max_profit
    return max_profit
