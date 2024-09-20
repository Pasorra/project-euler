def check(i):
    increasing = decreasing = True
    prev_digit = i % 10
    i //= 10
    while i > 0:
        current_digit = i % 10
        if current_digit > prev_digit:
            decreasing = False
        elif current_digit < prev_digit:
            increasing = False
        prev_digit = current_digit
        i //= 10
    return not (increasing or decreasing)


non_bouncy = 0
bouncy = 0
i = 1
while True:
    if check(i):
        bouncy += 1
    else:
        non_bouncy += 1

    if bouncy / (bouncy + non_bouncy) >= 0.99:
        print(i)
        break

    i += 1
