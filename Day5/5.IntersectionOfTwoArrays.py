def intersection(nums1, nums2):
    return list(set(nums1) and set(nums2))
# Test
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
