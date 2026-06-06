class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        box=[]
        result=1
        for i in range(len(nums)):
            result =1
            for j in range(len(nums)):
                if i!=j:
                    result=result*nums[j]
            box.append(result)
        return box