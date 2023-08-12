from utils import count_int_len

numerator = 1
denominator = 2
last_numerator = numerator
last_denominator = denominator

count = 0
for i in range(2, 1000 + 1):
    numerator, denominator = last_numerator, last_denominator
    numerator += 2 * denominator
    numerator, denominator = denominator, numerator
    last_numerator, last_denominator = numerator, denominator
    numerator += denominator
    if(count_int_len(numerator) > count_int_len(denominator)):
        count += 1
print(count)
