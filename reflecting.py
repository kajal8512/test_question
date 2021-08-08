O_l=[1,1,2,3,4,4,5,1]
i=0
c=0
k=[]
while i<len(O_l):
    j=0
    while j<i:
        if i==j:
            c+=1
            k.append(i)
            print(c,k)
            j+=1
        else:
            k.append(i)
        i+=1
