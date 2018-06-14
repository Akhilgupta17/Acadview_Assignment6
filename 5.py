num=list(range(1,101))
odd=[]
even=[]
for x in num:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(odd)
print(even)
