vs = "aeiou"

s = input("Enter a string: ")
for i in s:
    if(vs.find(i)>=0):
        print(i)

