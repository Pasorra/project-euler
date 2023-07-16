# AS SLOW AS IT GETS but it checks everything just to be sure ehe...
from itertools import permutations
from utils import sieve


primes = sorted(list(sieve(17 + 1)))

pandigitals = [list(x) for x in permutations([x for x in range(10)], 10)]
for i in range(len(pandigitals)):
    if pandigitals[i][0] == 0:
        continue
    lst = [int(''.join(map(str, pandigitals[i][x:x+3])))
           for x in range(1, len(pandigitals[i]) - 2)]
    lst.insert(0, pandigitals[i][0])
    pandigitals[i] = lst

count = 0
for num in pandigitals:
    check = True
    for i in range(1, 8):
        if num[i] % primes[i - 1] != 0:
            check = False
            break
    if check:
        arr = []
        for i in range(len(num) - 1):
            if len(str(num[i])) == 2:
                arr.append("0")
            else:
                arr.append(str(num[i])[0])
        arr.append(str(num[i + 1]))
        print(arr)
        no = int("".join(arr))
        print(no)
        count += no

print(count)
