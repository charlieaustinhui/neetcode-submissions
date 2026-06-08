class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()

        for i, n in enumerate(nums): 
                if n==nums[i-1] and i>0: 
                        continue
                l, r = i+1, len(nums)-1
                while l<r:
                        threeSum= n+nums[l]+nums[r]
                        if(threeSum<0):
                                l=l+1
                        elif(threeSum>0): 
                                r=r-1
                        else: 
                                result.append([n,nums[l],nums[r]])
                                l+=1
                                while nums[l]==nums[l-1] and l<r:
                                        l+=1
        return result

                