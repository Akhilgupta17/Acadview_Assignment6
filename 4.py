list=[]
list.append(1)
list.append(2)
list.append("Acadview")
list.append("class")
list.append(5.0)
list.append(7.5)
print(list)

s=[]
i=[]
f=[]

for x in list:
    if type(x)==str:
        s.append(x)
    elif type(x)==int:
        i.append(x)
    elif type(x)==float:
        f.append(x)
print(s)
print(i)
print(f)
