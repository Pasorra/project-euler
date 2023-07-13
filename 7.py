from utils import is_prime

prime_counter = 1
i = 3
while True:
    if is_prime(i): prime_counter += 1
    if prime_counter == 10001: 
        print(i) 
        break 
    i += 2


