l=[True,False,True,True,True,False]
i=0
d=0
c=0
k=[]
while i<len(l):
    if l[i]==True:
        c=c+1
        k.append(c)
    else:
        d+=1
        k.append(d)
    i+=1
if c>d:
    print(True)
else:
    print(False)