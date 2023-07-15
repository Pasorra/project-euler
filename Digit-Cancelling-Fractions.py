arr = []
for a in range(11, 100):
    for b in range(a + 1, 100):
        a = str(a)
        b = str(b)
        s = set(a + b)
        if "0" in s or len(s) == 4:
            continue
        same = ""
        for val in s:
            if val in a and val in b:
                same = val
                break
        x = a.replace(val, "", 1)
        y = b.replace(val, "", 1)
        if int(a) / int(b) == int(x) / int(y):
            arr.append((x, y))

top = 1
bottom = 1
for val in arr:
    top *= int(val[0])
    bottom *= int(val[1])

print(top/bottom)
