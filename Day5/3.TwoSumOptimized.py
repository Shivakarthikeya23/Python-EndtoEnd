def two_sum(nums, target):
    hm = {}
    for i, num in enumerate(nums):
        diff = target-num
        if diff in hm:
            return [hm[diff], i]
        hm[num] = i

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
