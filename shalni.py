''''list=["kajal","shalni","Neha","Nisha"]
list1=[0,1,2,3]
i=0
while i<len(list1):
    j=0
    while j<len(list):
        print(list1[i],list[j])
        j+=1
        i+=1'''

# list=["kajal","shalni","Neha","Nisha"]
# i=0
# while i<len(list):
#     print(i,list[i])
#     i+=1

user=input("enter the name")
i=0
while i<len(user):
    print(user.upper()[i]+user.lower()[i]*(i),end=" ")
    print("_",end="")
    i+=1




