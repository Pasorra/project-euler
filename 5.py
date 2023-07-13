from collections import defaultdict
from utils import factorize

product = defaultdict(int)
for i in range(1, 20 + 1):
    factors = factorize(i)
    for factor in set(factors):
        occurrence = factors.count(factor)
        product[factor] = max(occurrence, product[factor])

result = 1
for key, val in product.items():
    result *= key ** val

print(result)