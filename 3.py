def calculate_change(cost):
    coin_values = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    available_coins = {
        2.0: 2,
        1.0: 6,
        0.5: 10,
        0.2: 4,
        0.1: 6,
        0.05: 7,
        0.02: 4,
        0.01: 6
    }
    change = {}

    for value in coin_values:
        num_coins = min(int(cost / value), available_coins[value])
        cost -= num_coins * value
        available_coins[value] -= num_coins
        if num_coins > 0:
            change[value] = num_coins

    if cost == 0:
        return change
    else:
        return "Can't afford this with the available petty change"

# Test cases
print(calculate_change(12.50))
print(calculate_change(16.89))
print(calculate_change(16.90))
