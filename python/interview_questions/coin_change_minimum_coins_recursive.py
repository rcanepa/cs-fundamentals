"""Given a set of different coins denominations S and a total
T, find the smallest combination of coins that add up to total.

Example:
    S = {1, 5, 10, 25}, T = 40
    result = {5, 10, 25}

    S = {1, 5, 9, 20}, T = 27  <- Notice that a greedy algorithm would fail here
    result = {9, 9, 9}
"""


def find_number_of_min_coins(coins, target):
    cache = {}
    solutions = []

    def _find_solutions(current_solution, current_sum, coin_index):
        if (current_solution, current_sum, coin_index) in cache:
            return None
        else:
            cache[(current_solution, current_sum, coin_index)] = True

        if coin_index == len(coins):
            return None

        if current_sum == target:
            solutions.append(current_solution)
            return None

        curr_coin = coins[coin_index]
        _find_solutions(current_solution, current_sum, coin_index + 1)

        if current_sum + coins[coin_index] <= target:
            _find_solutions(current_solution + (curr_coin,), current_sum + curr_coin, coin_index)
            _find_solutions(current_solution + (curr_coin,), current_sum + curr_coin, coin_index + 1)

    _find_solutions((), 0, 0)

    solutions.sort(key=lambda s: len(s))

    return solutions[0]


if __name__ == "__main__":
    test_cases = [
        ([1], 3, [1, 1, 1]),
        ([1, 5, 10, 25], 40, [5, 10, 25]),
        ([1, 5, 9, 20], 27, [9, 9, 9]),
        ([1, 5, 6, 8], 11, [5, 6]),
        ([8, 5, 1, 6], 11, [5, 6]),
        ([8, 5, 1, 6, 2, 3, 4, 5, 6, 7], 11, [5, 6]),
    ]

    for input_coins, input_total, expected_result in test_cases:
        result = find_number_of_min_coins(input_coins, input_total)
        assert sorted(result) == sorted(expected_result)