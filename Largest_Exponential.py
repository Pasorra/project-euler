import math

arr = []
with open("texts/0099_base_exp.txt", "r") as f:
    for i, line in enumerate(f, 1):
        line = line.split(",")

        #compare logs instead of exponents
        base = int(line[0])
        exp = int(line[1])
        logged = exp * math.log(base, 10)

        arr.append([logged, i])
        
        
arr.sort(key=lambda x : x[0], reverse=True)
print(arr[0][0], arr[0][1])

