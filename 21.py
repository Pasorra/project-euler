def d(n):
    divisors_sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum


nums_and_sums = {}

for i in range(1, 10000):
    nums_and_sums[i] = d(i)

all_amicable = 0
for key, val in nums_and_sums.items():
    if val in nums_and_sums and nums_and_sums[val] == key and val != key:
        all_amicable += val

print(all_amicable)
