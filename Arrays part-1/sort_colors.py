def sortColors(nums): # take nums list as a Parameter
        index=0
        if (len(nums) == 1):
            return nums #if their is one number in a list simply return that one number
        def ChangeIndex(array,index,place): #change the position based on the value
            tem=array[index]
            popElement=nums.pop(index)
            array.insert(place,tem)

        for i in range(len(nums)):
            if(nums[index] == 2):
               ChangeIndex(nums,index,len(nums)) #if the number is 2 then append last in the list
            elif(nums[index] == 0):
                if(index!=0):
                    ChangeIndex(nums,index,0) #if the number is 0 then append first in the list
                    index+=1
                else:
                    index+=1
            else:
                if(index == 0 and nums[1] == 0):  #incase list[1] is 0 simply swap 1 and 0
                    nums[0],nums[1]=nums[1],nums[0]
                else:
                    x=1
                    while(nums[x] == 1 or nums[x] == 2): #if 1 is staring position then change that number with 0
                        if(x == len(nums)-1): #if list not having the 0 then break the loop
                            break
                        else:
                            x+=1 #otherwise increase the index value
                    if(x!=len(nums) and nums[x]==0): #if found first 0 in the list then swap ,otherwise not swap
                        nums[0],nums[x]=nums[x],nums[0]
                index+=1   #if number is 1 then skip
        return nums

print(sortColors([1,0,1,2,2,1,0,2,1,0,1,0])) #give nums list as a Argument to the sortColors function
    