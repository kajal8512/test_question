b=[[1,2,3,],[1,2,3],[2,3,4,5],[4,5,6]]
i=0
s=0
while i<len(b):
    j=0
    while j<len(b[i]):
        c=b[i][j]
        s=s+c
        j+=1
    i+=1
print(s)
