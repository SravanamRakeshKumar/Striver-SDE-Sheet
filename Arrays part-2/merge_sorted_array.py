def merge(nums1, m, nums2, n):
        if len(nums1) == nums1.count(0):
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
        else:
            for i in range(n):
                nums1.pop()
            for i in range(len(nums2)):
                for j in range(len(nums1)):
                    if(nums1[j]>=nums2[i]):
                        nums1.insert(j,nums2[i])
                        break
                if(j == len(nums1)-1):
                    nums1.insert(j+1,nums2[i])  
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
merge(nums1,m,nums2,n)
print(nums1)

