from itertools import permutations
from utils import is_prime


for i in range(10, 1, -1):
    x = [int("".join(map(str, x))) for x in permutations(range(1, i), i - 1)]
    x.reverse()
    for num in x:
        if not is_prime(num):
            continue
        if len(str(num)) == len(set(str(num))):
            print(num)
            exit()
