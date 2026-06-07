class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        box=set(nums)
        longest=0
        for n in nums: 
            if n-1 not in box:
                length=0
                while n+length in box:
                    length+=1
                longest = max(longest, length)
        return longest 
                