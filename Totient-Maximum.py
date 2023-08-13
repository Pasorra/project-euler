from utils import is_prime

i, n = 3, 2
while n <= 1_000_000:
    if is_prime(i):
        n *= i
    i += 2
n /= (i - 2)
print(n)
