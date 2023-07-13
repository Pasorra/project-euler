with open("names.txt", "r") as f:
    names = f.readlines()[0].split(",")


names.sort()
total = 0
for i, name in enumerate(names):
    name = name.strip("\"")
    val = 0
    for character in name:
        val += (ord(character) - 64)
    total += val * (i + 1)

print(total)
