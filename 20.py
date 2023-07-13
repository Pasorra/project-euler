factor = 1
for i in range(2, 100 + 1):
    factor *= i

result = 0
for x in str(factor):
    result += int(x)

print(result)