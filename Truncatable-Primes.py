from utils import is_prime


def check(num, memo):
    if num not in memo:
        return False
    num_str = str(num)
    if len(num_str) == 1:
        return True
    for i in range(1, len(num_str)):
        if (num // (10 ** i) not in memo) or (num % (10 ** i) not in memo):
            return False
    return True


total = 0
count = 0
i = 11
memo = {2, 3, 5, 7}
while count != 11:
    if is_prime(i):
        memo.add(i)
        if check(i, memo):
            print("Found: ", i)
            count += 1
            total += i
    i += 2

print(total)
