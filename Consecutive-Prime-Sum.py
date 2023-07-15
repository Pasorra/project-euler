from utils import sieve

primes = sorted(list(sieve(1_000_000)))

total = 0
longest = 0
result = 0
start = 0
end = 0

while end < len(primes):
    total += primes[end]
    end += 1
    if total > 1_000_000:
        val = primes[start]
        total -= val
        start += 1
        while total > 1_000_000:
            end -= 1
            val = primes[end]
            total -= val

    if end - start > longest and total in primes:
        longest = end - start
        result = total

print(longest)
print(result)
