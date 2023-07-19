import numpy
from math import sqrt


def factorize(num: int):
    """Returns the prime factors of a positive integer as a list."""
    factors = []
    x = 2
    while num > 1:
        if num % x == 0:
            factors.append(x)
            num /= x
        else:
            x += 1
    return factors


def completely_factorize(num: int):
    """Takes a positive integer and returns all its divisors including 1."""
    if num < 0:
        return []
    factors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors


def is_palindrome(val: str) -> bool:
    val = str(val)
    i = 0
    for i in range(int(len(val))):
        left = val[i]
        right = val[len(val) - i - 1]
        if left != right:
            return False
    return True


def is_prime(num: int) -> bool:
    if num <= 1 or (num % 2 == 0 and num != 2):
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def sieve(n: int) -> set:
    """Returns a set of prime numbers up to 'n' (exclusive)."""
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        if flags[i]:
            flags[i*i::i] = False
    return set(numpy.flatnonzero(flags))


def count_prime_factors(num: int) -> int:
    """Returns the number of distinct prime factors of an integer."""
    num = abs(num)
    count = 0
    x = 2
    counted = False
    while x*x < num:
        if num % x == 0:
            count += 1 if not counted else 0
            counted = True
            num /= x
        else:
            counted = False
            x += 1

    return count + 1
