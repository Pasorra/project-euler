from utils import is_prime


d = 0
max_cycle = 0
for i in range(7, 1000, 2):
    if not is_prime(i):
        continue
    k = 1
    while True:
        if (10 ** k) % i == 1:
            d = i if k > max_cycle else d
            max_cycle = k if k > max_cycle else max_cycle
            break
        k += 1
print(d)
print(max_cycle)
