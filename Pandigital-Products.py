mem = {}


def should_continue(x, amount_of_digits):
    while x > 0:
        amount_of_digits += 1
        x //= 10
        if amount_of_digits > 9:
            return amount_of_digits
    return amount_of_digits


# just to be sure, 10000 works fine
for y in range(1, 1000000):
    for x in range(1, 1000000):
        res = x * y
        amount_of_digits = 0
        amount_of_digits = should_continue(res, amount_of_digits)
        if amount_of_digits > 9:
            break
        amount_of_digits = should_continue(x, amount_of_digits)
        if amount_of_digits > 9:
            break
        amount_of_digits = should_continue(y, amount_of_digits)
        if amount_of_digits > 9:
            break
        s = set(str(res) + str(x) + str(y))
        if len(s) != 9 or "0" in s:
            continue
        mem[res] = 1

result = 0
for x in mem.keys():
    result += x

print(result)
