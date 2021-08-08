list=[10,20,30,40]
list1=[100,200,300,400]
i=0
while i<len(list):
    j=1
    while j<=len(list1):
        print(list[i],list1[-j])
        j+=1
        i+=1