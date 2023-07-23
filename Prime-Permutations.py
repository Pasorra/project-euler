from itertools import permutations
from utils import is_prime

for i in range(1000, 9999 + 1):
    correct = True
    arr = [str(i), str(i + 3330), str(i + 6660)]
    perms = ["".join(x) for x in permutations([x for x in str(i)], 4)]

    temp_arr = []
    for num in arr:
        if num not in perms or not is_prime(int(num)):
            correct = False
            break
    if correct:
        print("".join(arr))
