arr=[3,2,1]
answer=0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            answer+=1
print(answer)