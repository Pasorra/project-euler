from utils import sieve, is_prime

n = 1000
arr = []
primes = sieve(10_000)
for prime in primes:
    for x in range(n):
        x = 2 * (x * x)
        res = x + prime
        arr.append(res)

for i in range(3, n * 10, 2):
    if i not in arr and i not in primes:
        print(i)
        break
