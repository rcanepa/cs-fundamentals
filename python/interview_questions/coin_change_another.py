def make_change(coins, change):
    solutions = set()

    def _change(left, solution, index=0):
        if left == 0:
            solutions.add(solution)

        if left < 0:
            return

        for i in range(index, len(coins)):
            c = coins[i]
            _change(left - c, solution + (c, ), i)
    _change(change, (), 0)
    return solutions


if __name__ == "__main__":
    coins = [2, 3, 9, 10]
    change = 27
    result = make_change(coins, change)

    if result:
        print("Solutions found:", len(set(result)))
        for sol in result:
            print("-> ", sol, "=", sum(sol))
