import functional as F

def stock_history(init_investment, monthly_contribution, stock_prices):
    stock_prices = F.map(stock_prices,
                         F.pipe(lambda x: x.split(" "),
                                lambda x: [int(a) for a in x]))

    sell_prices = stock_prices[-1]

    total_earning = 0
    total_investment = 0
    max_earning_rate = [1 for _ in sell_prices]

    for month in range(len(stock_prices) -2, -1, -1):
        current_prices = stock_prices[month]
        earning_rate = [sell_prices[i] / price for i, price in enumerate(current_prices)]
        max_earning_rate = [max(a, b) for a, b in zip(max_earning_rate, earning_rate)]

        money = init_investment if month == 0 else monthly_contribution
        total_earning += money * max(max_earning_rate)
        total_investment += money

    return int(round(total_earning - total_investment))

print(stock_history(1000, 0, ["10 20 30",
                              "15 24 32"]))
print(stock_history(1000, 0, ["10", "9"]))
print(stock_history(100, 20, ["40 50 60",
                              "37 48 55",
                              "100 48 50",
                              "105 48 47",
                              "110 50 52",
                              "110 50 52",
                              "110 51 54",
                              "109 49 53" ]))