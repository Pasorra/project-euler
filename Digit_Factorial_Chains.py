fact_memo = {}


def fact_w_memo(i, memo):
    if i in memo:
        return memo[i]
    if i <= 1:
        return 1
    res = i * fact_w_memo(i - 1, memo)
    memo[i] = res
    return res


def recursively_check(num, loop: set):
    if num in loop:
        return len(loop)
    loop.add(num)
    res = 0
    while num != 0:
        a = num % 10
        res += fact_w_memo(a, fact_memo)
        num //= 10
    return recursively_check(res, loop)


res = 0
for i in range(1, 1_000_000 + 1):
    if recursively_check(i, set()) == 60:
        res += 1
print(res)
