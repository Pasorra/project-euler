from math import sqrt


def factorize(num: int):
    """Takes a positive integer and returns its factors as a list."""
    factors = []
    x = 2
    while num > 1:
        if num % x == 0:
            factors.append(x)
            num /= x
        else:
            x += 1
    return factors

def is_palindrome(val: str):
    val = str(val)
    i = 0
    for i in range(int(len(val))):
        left = val[i]
        right = val[len(val) - i - 1] 
        if left != right: return False
    return True

def is_prime(num: int):
    if num % 2 == 0 and num != 2: return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0: return False
    return True