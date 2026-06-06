class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums={}
        for i in range(len(nums)):
            n=nums[i]
            difference=target-n
            if difference in prevNums:
                return [prevNums[difference],i]
            prevNums[n]=i
        return
        