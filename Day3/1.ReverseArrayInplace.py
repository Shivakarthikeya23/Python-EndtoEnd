l = [1, 2, 3,4,5]
def reverse(arr):
    s,e=0, len(arr)-1
    while(s<e):
        t = arr[s]
        arr[s]=arr[e]
        arr[e]=t
        s+=1
        e-=1
    return arr


print(reverse(l))
#   print(l[::-1])