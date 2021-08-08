b=[[1,2,3],[1,2,3]]
i=0
k=[]
while i<len(b):
    j=0
    while j<len(b[i]):
        c=b[i][j]*b[i][j]
        k.append(c)
        j+=1
    print(k)
    i+=1
    break
