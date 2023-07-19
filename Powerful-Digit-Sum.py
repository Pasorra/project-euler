result = 0
res_a = 0
res_b = 0
for a in range(2, 100):
    for b in range(2, 100):
        val = a**b
        accum = 0
        while val > 0:
            accum += val % 10
            val //= 10
        if accum > result:
            result = accum
            res_a = a
            res_b = b
print(result)
print(res_a, res_b)
