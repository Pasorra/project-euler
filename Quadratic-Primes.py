from utils import is_prime

longest = 0
longest_product = 0
for b in range(1000 + 1):
    if not is_prime(b):
        continue
    for a in range(-1000, 1000 + 1):
        if b != 2 and a % 2 == 0:
            continue
        x = 0
        while is_prime((x ** 2) + (a * x) + b):
            x += 1
            if x > longest:
                longest = x
                longest_product = a * b

print(longest_product)
