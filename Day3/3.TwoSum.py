def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    pair = {}
    for i, num in enumerate(nums):
        if target - num in pair:
            return [i, pair[target - num]]
        pair[num] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
