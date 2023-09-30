n, d = 2, 5
while d <= 1_000_000:
    n += 3
    d += 7
print(n - 3, d - 7)

"""
Used below code to see the pattern, numerator goes up by 3 and denominator goes up by 7
"""
# from utils import gcd

# arr = []
# memo = set()
# three_over_seven = 3/7
# for d in range(1, 19 + 1):
#     for n in range(1, d):
#         n_over_d = n/d
#         if (n_over_d in memo) or (three_over_seven < n_over_d):
#             continue

#         divisor = gcd(n, d)
        
#         if(divisor == 1):
#             arr.append([n_over_d, n , d])
#             memo.add(n_over_d)

# arr.sort(key=lambda x: x[0])
# for i in range(len(arr)):
#     n = arr[i][1]
#     d = arr[i][2]
#     if(n == 3 and d == 7):
#         n = arr[i - 1][1]
#         d = arr[i - 1][2]
#         print(str(n) + " / " + str(d) + " = ", arr[i - 1][0])
#         exit()

