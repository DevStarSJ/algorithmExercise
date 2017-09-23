import math

def interest_rate(price, monthly_payment, loan_term):
    total_payment = monthly_payment * loan_term
    if price == total_payment:
        return 0

    rate_range = [0, 100]
    before_rate = 0
    current_rate = 50

    while math.fabs(current_rate - before_rate) > 0.0000000000000000000000000000000001:

        result = calc_payment(price, monthly_payment, loan_term, current_rate)

        if result > 0:
            rate_range = [current_rate, rate_range[1]]
        elif result < 0:
            rate_range = [rate_range[0], current_rate]
        else:
            return current_rate
        before_rate = current_rate
        current_rate = (rate_range[1] - rate_range[0]) / 2 + rate_range[0]

    return current_rate

def calc_payment(price, monthly_payment, loan_term, yearly_rate):
    monthly_rate = yearly_rate / 12
    rest_price = price

    for i in range(loan_term):
        this_rate = rest_price * monthly_rate / 100
        return_price = monthly_payment - this_rate
        rest_price -= return_price

    return 1 if rest_price < 0 else -1 if rest_price > 0 else 0

print(interest_rate(6800,100,68))
print(interest_rate(2000,510,4))
print(interest_rate(15000,364,48))


