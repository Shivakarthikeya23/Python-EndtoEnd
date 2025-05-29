l = [1, 2,4,5,6,7,8,10]
def sumEven(l):
    s=0
    for i in l:
        if i%2==0:
            s+=i
    return s

print(sumEven(l))