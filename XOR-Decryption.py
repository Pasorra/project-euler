with open("texts/0059_cipher.txt", "r") as f:
    data = [int(x) for x in f.readline().split(",")]

for key1 in range(97, 122 + 1):
    for key2 in range(97, 122 + 1):
        for key3 in range(97, 122 + 1):
            temp_str = []
            result = []
            result_ascii = []
            keys = [key1, key2, key3]
            i = 0
            for val in data:
                val = val ^ keys[i]
                result_ascii.append(val)
                i = (i + 1) % 3
                if(chr(val) == " "):
                    result.append("".join(temp_str))
                    temp_str = []
                else:
                    temp_str.append(chr(val))
            if("and" in result and "is" in result and "the" in result):
                print(" ".join(result))
                print(sum(result_ascii))
                exit()
