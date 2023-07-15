from math import sqrt

memo = {}

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        if a + b > 1000:
            break
        c = sqrt(a ** 2 + b ** 2)
        total = int(a + b + c)
        if c % 1 == 0 and total <= 1000:
            try:
                memo[total] += 1
            except:
                memo[total] = 1

print(max(memo, key=lambda x: memo[x]))
