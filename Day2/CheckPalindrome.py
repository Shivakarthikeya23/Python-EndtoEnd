def isPalindrome(st):
    s, e=0,len(st)-1
    while(s<=e):
        if(st[s]!=st[e]):
            return False
        s+=1
        e-=1
    return True

s = input("Enter a string: ")
print(isPalindrome(s))
