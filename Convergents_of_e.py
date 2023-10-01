import math


convergents = [2, 1]
x = 2
for i in range(98):
    if i % 3 == 0:
        convergents.append(x)
        x += 2
    else:
        convergents.append(1)
    
numerator = 1
denominator = convergents[-1]

        
for i in range(len(convergents) - 2, -1, -1):
    numerator = (denominator * convergents[i]) + numerator
    numerator, denominator = denominator, numerator
    
numerator, denominator = denominator, numerator    

print(numerator, denominator, numerator/denominator, math.e)
result = 0
while numerator > 0:
    result += numerator % 10
    numerator //= 10
print(result)
    