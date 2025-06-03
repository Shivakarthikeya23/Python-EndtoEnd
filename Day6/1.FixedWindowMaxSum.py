def max_sum_fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide window
        max_sum = max(max_sum, window_sum)

    return max_sum


# Test
print(max_sum_fixed_window([2, 1, 5, 1, 3, 2], 3))  # Output: 9
