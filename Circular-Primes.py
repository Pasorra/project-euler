from utils import is_prime


def combs(num):
    num = list([str(x) for x in str(num)])
    for _ in range(len(num) - 1):
        val = num.pop()
        num.insert(0, val)
        yield "".join(num)


count = 1
for i in range(3, 1_000_000, 2):
    if not is_prime(i):
        continue
    for num in combs(i):
        if not is_prime(int(num)):
            break
    else:
        count += 1

print(count)
