from utils import factorize

i = 1
while True:
    i1 = str(i)
    i2 = str(i*2)
    i3 = str(i*3)
    i4 = str(i*4)
    i5 = str(i*5)
    i6 = str(i*6)
    if len(i1) == len(i2) == len(i3) == len(i4) == len(i5) == len(i6):
        if set(i1) == set(i2) == set(i3) == set(i4) == set(i5) == set(i6):
            print(i)
            break
    i += 1
