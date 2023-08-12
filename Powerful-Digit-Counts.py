from utils import count_int_len

count = 0
for x in range(1, 100):
    for power in range(1, 100):
        num = x ** power
        int_len = count_int_len(num)
        if(power != count_int_len(num)):
            continue
        count += 1

print(count)
