combinations = []


def combine(combinations, nums: list = None):
    if nums is None:
        nums = []
    if len(nums) == 10:
        combinations.append("".join(nums))
        return
    for i in range(10):
        i = str(i)
        if i in nums:
            continue
        nums.append(i)
        combine(combinations, nums)
        nums.remove(i)


combine(combinations)
combinations.sort()
print(combinations[999_999])
