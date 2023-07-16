from itertools import permutations
from utils import sieve


primes = sorted(list(sieve(17 + 1)))

count = 0
pandigitals = [list(x) for x in permutations([str(x) for x in range(10)], 10)]
for i in range(len(pandigitals)):
    flag = True
    if pandigitals[i][0] == 0:
        continue
    for x in range(1, len(pandigitals[i]) - 2):
        val = int("".join(pandigitals[i][x:x+3]))
        if val % primes[x - 1] != 0:
            flag = False
            break
    if flag:
        count += int("".join(pandigitals[i]))

print(count)
