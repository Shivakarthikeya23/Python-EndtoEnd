def most_frequent_element(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num, 0)+1

    maxFreq = max(freq.values())

    for key in freq:
        if freq[key]==maxFreq:
            return key

print(most_frequent_element([1, 3, 1, 3,3,3,3,4, 2, 1]))  # Output: 3
