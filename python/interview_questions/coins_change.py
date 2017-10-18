""" Coin/Change problem
Given a set of coins and a change, compute the change with the smallest
number of coins.

This solution allows duplicated coins and compute all the possible
solutions.
"""


def make_change(coins, change):
    solutions = []

    def _make_change(coins_path, index, change_left):
        if change_left == 0:
            solutions.append(coins_path)
        else:
            for ci in range(index, len(coins)):
                if coins[ci] <= change_left:
                    _make_change(coins_path + (coins[ci],), ci, change_left - coins[ci])

    _make_change((), 0, change)
    return solutions


if __name__ == "__main__":
    coins = [2, 3, 9, 10]
    change = 27

    result = make_change(coins, change)

    if result:
        print("Solutions found:", len(set(result)))
        for sol in result:
            print("-> ", sol, "=", sum(sol))
        smallest_solution = result[0]
        for i in range(1, len(result)):
            if len(smallest_solution) > len(result[i]):
                smallest_solution = result[i]
        print("Best solution:", smallest_solution)
    else:
        print("No solution was found!")
