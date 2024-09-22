memo = set()
n = 1
d = 3
count = 0
while d <= 12000:
    frac = n / d
    while frac < 0.5:
        if (1 / 3 < frac < 1 / 2) and (frac not in memo):
            count += 1
            memo.add(frac)
        n += 1
        frac = n / d
    n = 1
    d += 1
print(count)
