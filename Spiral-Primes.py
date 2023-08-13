from utils import is_prime


num = 1
i = 2
primes = 0
diagonal_numbers = 1
while True:
    for _ in range(4):
        num += i
        if is_prime(num):
            primes += 1
        diagonal_numbers += 1
        ratio = primes/diagonal_numbers * 100
        if(primes/diagonal_numbers * 100 < 10):
            print("Primes: " + str(primes) +
                  " Total no of diagonal numbers: " + str(diagonal_numbers))
            print("Number of sides " + str(i + 1))
            exit()
    i += 2
