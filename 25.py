last = 1
current = 1
i = 3
while True:
    temp = last
    last = current
    current += temp
    if len(str(current)) >= 1000:
        print(i)
        break
    i += 1