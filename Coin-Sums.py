arr = [1, 2, 5, 10, 20, 50, 100, 200]


def solve(x=0, min_coin=1):
    if x == 200:
        return 1
    elif x > 200:
        return 0
    total = 0
    for i in arr:
        if i >= min_coin:
            total += solve(x + i, i)
    return total


print(solve())
