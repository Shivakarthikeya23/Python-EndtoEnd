from collections import defaultdict


def group_anagrams(strs):
    hm = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        hm[key].append(s)
    return list(hm.values())



print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
