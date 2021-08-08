a=[1,2,3,4,5,6]
i=0
k=[]
while i<len(a):
    b=str(a[i])+str(a[i+1])
    k.append(b)
    i+=2
print(k)
    