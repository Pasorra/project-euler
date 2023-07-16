from math import sqrt


def pentagonal(x, memo):
    if x in memo:
        return True
    val = (1 + sqrt((24*x) + 1))
    if val % 6 == 0:
        memo.add(x)
        return True
    return False


memo = set()
z = 1
while True:
    x = z * (3 * z - 1) // 2
    for y in range(1, z):
        y = y * (3*y - 1) // 2
        if pentagonal(x - y, memo) and pentagonal(x + y, memo):
            print(x - y)
            exit()
    z += 1
