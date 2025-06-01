nums = [0,1,0,2,4,5,0,7]


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    s, c = 0, 0
    for i in range(len(nums)):
        if (nums[i] != 0):
            nums[s] = nums[i]
            s += 1
        else:
            c += 1
    for i in range(len(nums) - 1, len(nums) - c - 1, -1):
        nums[i] = 0

moveZeroes(nums)

print(nums)