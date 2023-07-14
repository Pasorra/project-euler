n = 100
nums = set()
for a in range(2, n + 1):
    for b in range(2, n + 1):
        nums.add(a**b)

print(len(nums))
