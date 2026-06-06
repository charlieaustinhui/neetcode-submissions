class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums={}
        for i, n in enumerate(nums):
            difference=target-n
            if difference in prevNums:
                return [prevNums[difference],i]
            prevNums[n]=i
        return
        