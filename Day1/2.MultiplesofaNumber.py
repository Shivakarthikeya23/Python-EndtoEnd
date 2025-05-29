def printTable(n, limit):
    for i in range(1, limit+1):
        print(n , " X " , i, " = ",  n*i )

while(True):
    n=int(input("Enter a number to get multiples or 0 to exit: "))
    if(n==0):
        break
    printTable(n, 10)
