from math import factorial


fact_memo = {str(x): factorial(x) for x in range(10)}
result = 0
for i in range(3, 10000000):
    i = str(i)
    total = 0
    for digit in i:
        total += fact_memo[digit]
    if total == int(i):
        result += total

print(result)
