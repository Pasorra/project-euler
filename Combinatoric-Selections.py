from math import factorial, prod


def check(i, x):
    while x < i:
        top = prod([n for n in range(i, i - x, -1)])
        bottom = factorial(x)
        if top // bottom > 1_000_000:
            return (i + 1) - (x * 2)
        x += 1
    return 0


count = 0
for i in range(23, 100 + 1):
    x = 1
    count += check(i, x)

print(count)
