def isPrime(n):
    if(n<=1):
        return False
    for i in range(2, int(pow(n, 1/2))+1):
        if(n%i==0):
            return False
    return True

while(True):
    n = int(input("Enter a number to check Prime or 0 to Exit: "))
    if(n==0):
        break
    print(isPrime(n))