def findDuplicate(nums):
    temp=[0]*(len(nums)+1)
    for i in range(len(nums)):
        if temp[nums[i]-1] == 0 :
            temp[nums[i]-1]=1
        else:
            return nums[i]
nums=[1,3,4,2,2]
print(findDuplicate(nums))

            
        