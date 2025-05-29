def removeDup(l):
    l2=[]
    for i in l:
      if(l2.count(i)==0):
          l2.append(i)
    return l2

l1 = [1,2,2,3,4,4,5,6,7,7,8]
print(removeDup(l1))