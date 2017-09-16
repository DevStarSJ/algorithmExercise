coins = [100, 50, 20, 10, 5, 2, 1]
goal = 200

def get_ways(coins, goal):
    if goal == 0 or coins[0] == 1:
        return 1
    ways = 0
    for a in range(goal//coins[0] + 1):
        rest = goal - a * coins[0]
        ways += get_ways(coins[1:], rest)
    return ways

print(get_ways(coins, goal) + 1)