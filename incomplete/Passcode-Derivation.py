with open("0079_keylog.txt", "r") as f:
    data = [(x).strip("\n") for x in f.readlines()]

chunks = [{}, {}, {}]
unique_characters = set()
for val in data:
    for i, character in enumerate(val):
        unique_characters.add(character)
        try:
            chunks[i][character] += 1
        except:
            chunks[i][character] = 1

for i, chunk in enumerate(chunks):
    sorted_items = sorted(
        chunk.items(), key=lambda item: item[1], reverse=True)
    chunks[i] = sorted_items

result = [[] for _ in range(len(unique_characters))]
# result[0] = chunks[0][0][0]
# result[-1] = chunks[-1][0][0]
# del chunks[0][0]
# del chunks[-1][0]
for i in range(len(result) - 2):
    result[i].append(chunks[0][i])
    result[i + 1].append(chunks[1][i])
    result[i + 2].append(chunks[2][i])

for r in result:
    print(r)
