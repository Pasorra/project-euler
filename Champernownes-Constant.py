arr = []
i = 1
while True:
    if len(arr) > 1000000:
        break
    arr.append(str(i))
    i += 1

arr = "".join(arr)
print(int(arr[1 - 1]) * int(arr[10 - 1]) * int(arr[100 - 1]) * int(arr[1000 - 1])
      * int(arr[10000 - 1]) * int(arr[100000 - 1]) * int(arr[1000000 - 1]))

print(arr[1 - 1], arr[10 - 1], arr[100 - 1], arr[1000 - 1],
      arr[10000 - 1], arr[100000 - 1], arr[1000000 - 1])
