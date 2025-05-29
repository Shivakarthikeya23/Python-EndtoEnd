def stringCompress(s):
    i = 0
    res=""
    while (i < len(s)):
        ch = s[i]
        c=0
        while (i < len(s) and ch == s[i]):
            c+=1
            i+=1
        res+=ch
        res+=str(c)
    return res

print(stringCompress("aaabbccdaabbbbc"))