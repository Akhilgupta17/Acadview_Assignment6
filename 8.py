list=[]
for i in range(0,5):
    num=int(input("Enter Number:"))
    list.append(num)
    print(list)

x=int(input("Enter Element:"))
if x in list:
    list.remove(x)
    print(list)
    

        
