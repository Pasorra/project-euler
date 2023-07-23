from utils import reverse_num


def lychrel(num, iter=1):
    if iter > 50:
        return 1
    reversed_num = reverse_num(num)
    if num == reversed_num:
        return 0
    return lychrel(num + reversed_num, iter + 1)


count = 0
for i in range(1, 10_000):
    count += lychrel(i + reverse_num(i))

print(count)
