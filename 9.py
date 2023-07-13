from math import sqrt

for a in range(1000):
    for b in range(1000):
        if b < a: continue
        c = sqrt(a ** 2 + b ** 2)
        if c % 1 == 0 and a + b + c == 1000: 
            print(a, b, int(c)) 
            print(a * b * c)
    
 