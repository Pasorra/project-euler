total = 1
for n in range(2, 10, 2):
    bottom_left = (n**2) + 1
    bottom_right = bottom_left - n
    top_right = (n+1) ** 2
    top_left = top_right - n
    print(bottom_left + bottom_right + top_right + top_left)
    total += bottom_left + bottom_right + top_right + top_left

print(total)
