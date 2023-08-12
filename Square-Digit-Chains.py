def check(num, memo):
    new_num = 0
    temp_num = num
    while num > 0:
        new_num += (num % 10) ** 2
        num //= 10
    if(new_num in memo):
        memo[temp_num] = memo[new_num]
        return memo[temp_num]
    if(new_num == 89):
        memo[temp_num] = 1
        return 1
    if(new_num == 1):
        memo[temp_num] = 0
        return 0
    res = check(new_num, memo)
    memo[temp_num] = res
    return res


count = 0
memo = {}
for i in range(2, 10_000_000 + 1):
    count += check(i, memo)

print(count)
