from utils import is_palindrome

total = 0
for i in range(1_000_000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        total += i

print(total)
