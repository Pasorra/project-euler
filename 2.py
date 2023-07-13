last = 1
current = 1
total = 0
while current <= 4_000_000:
    if current % 2 == 0: total += current
    temp = last
    last = current
    current += temp

print(total)

    