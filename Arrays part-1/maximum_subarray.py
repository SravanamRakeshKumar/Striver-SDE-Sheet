def maxSubArray(nums): #take nums list as a Parameter
        max_subarray=0 #default max_sub_array
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i] 
            if(sum<0): #ignore -number because it is decrease the subarray summ
                sum=0   #it means cut the subarray and agian start the sum to find the maxsubarray
            if(max_subarray<sum):
                max_subarray=sum #check the privious max_subarray for maxsubarray
        if (len(nums)>=1 and max_subarray == 0 and sum == 0): #list dos not maxsubarray then return the maximun value in the list
            return max(nums) 
        return max_subarray
print(maxSubArray([1,-1,2,0,4,2,1])) #give  list as a Argument to the maxSubArray function
        

        