with open("texts/0042_words.txt", "r") as f:
    words = [word.strip("\"") for word in f.readline().split(",")]

memo = {}


def calculate(num, n, memo):
    x = 0
    while num > x:
        x = (n * (n + 1)) // 2
        memo[n] = x
        n += 1
    return n


count = 0
last_n = 1
for word in words:
    val = 0
    for character in word:
        val += ord(character) - 64
    last_n = calculate(val, last_n, memo)
    if val in memo.values():
        count += 1

print(count)
