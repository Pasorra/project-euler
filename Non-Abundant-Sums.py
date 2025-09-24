# VERY inefficient, sorry :c

from utils import sieve


s = sieve(1_000_000)


def is_abundant(num: int) -> bool:
    s = 0
    for x in range(2, num, 1):
        if num % x == 0:
            s += x

    return s > num


abundants = set()

for i in range(28_124):
    if i in s:
        continue
    if is_abundant(i):
        abundants.add(i)

abundant_sums = set()

for y in abundants:
    for x in abundants:
        abundant_sums.add(x + y)

res_set = set(range(1, 28_123 + 1)) - abundant_sums

print(sum(res_set))
