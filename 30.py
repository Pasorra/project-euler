total = 0
# no idea how to rationalize other than check a million numbers, probably numbers become much bigger than the 5th powers summed after that
for i in range(2, 1_000_000):
    a = 0
    for digit in str(i):
        a += int(digit) ** 4
    if a == i:
        total += i

print(total)
