def sumofN(n):
    return n*(n+1)/2

def sumWithDigits(n, s, v):
    if(n<=1):
        print(s+"1"+"=", v+1)
        return
    sumWithDigits(n-1,s+str(n)+"+", v+n)

while(True):
    n = int(input("Enter a number or 0 to exit: "))
    if(n==0):
        break
    print(sumofN(n))
    print("With all Digits: ")
    sumWithDigits(n, "5+", 0)

