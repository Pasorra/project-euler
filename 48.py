result = 0
for i in range(1, 1000 + 1):
    result += (i ** i)
    result = result % 10000000000

print(result)