A=[3 ,1, 2,5 ,3] 
temp=[0]*(len(A))
for i in A:
    if temp[i-1] == 0:
        temp[i-1]=i
    else:
        repeated_Number=i
print([repeated_Number,temp.index(0)+1])