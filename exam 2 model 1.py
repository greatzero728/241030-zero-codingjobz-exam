def create_staircase(nums):
    while len(nums) != 0:
        step = 1
        subsets = []
    if len(nums) >= step:
        subsets.append(nums[0:step])
        nums = nums[step:]
        step += 1
    else:
        return False
    return subsets

nums = [1, 2, 3, 4, 5, 6, 7]
result = create_staircase(nums)
print(result)