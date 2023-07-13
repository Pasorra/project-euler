from utils import factorize

n = 2
while True:
    triangular = (n * (n + 1)) // 2
    factors = factorize(triangular)
    divisors = 1
    for factor in set(factors):
        occurrence = factors.count(factor) + 1
        divisors *= occurrence
    if divisors > 500:
        print(triangular)
        break
    n += 1
    