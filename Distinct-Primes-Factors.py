from utils import count_prime_factors

x = 10
while True:
    arr = [x, x+1, x+2, x+3]
    for i, val in enumerate(arr):
        if count_prime_factors(val) != 4:
            x += i + 1
            break
    else:
        print(x)
        break
