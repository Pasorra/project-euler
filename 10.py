from utils import is_prime


result = 2
for i in range(3, 2_000_000, 2):
    if is_prime(i): result += i

print(result)