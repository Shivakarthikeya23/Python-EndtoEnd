
while(True):
    n = int(input("Enter a number: "))
    if(n<0):
        print("Negative")
    elif(n>0):
        print("Positive")
    else:
        print("Its a Zero man")
    print("Exit")
    k = int(input("Enter a 0 to exit or 1 to continue: "))
    if(k==0):
        break
