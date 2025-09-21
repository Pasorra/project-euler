import time

n = 1000000000

start_time = time.time()


def check(num: int) -> bool:
    numstr = str(num)
    skip = False
    i = 1
    for c in numstr[:-1]:
        if skip:
            skip = False
            continue
        if c != str(i):
            return False
        skip = True
        i += 1

    return numstr[-1] == "0"


while True:
    if check(n * n):
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Number was: ", n)
        print(f"Time taken: {elapsed_time:.2f} seconds")
        break
    n += 1
