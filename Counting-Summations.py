memo = {}


def generate(target: int, amount_of_nums_used: int, last_used: int) -> int:
    if target == 0:
        if amount_of_nums_used > 1:
            return 1
    if target <= 0:
        return 0

    k = (target, amount_of_nums_used, last_used)
    if k in memo:
        return memo[k]

    res: int = 0
    for i in range(1, target + 1):
        if not amount_of_nums_used or i <= last_used:
            res += generate(target - i, amount_of_nums_used + 1, i)
        else:
            break
    memo[k] = res
    return res


target = 100
print(target, " : ", generate(target, 0, target))
