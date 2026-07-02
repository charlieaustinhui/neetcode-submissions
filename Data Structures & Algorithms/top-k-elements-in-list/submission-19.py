class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker={}
        frequency=[[]for i in range(len(nums)+1)]
        for n in nums: 
            tracker[n]=tracker.get(n,0)+1
        for n, c in tracker.items(): 
            frequency[c].append(n)
        result=[]
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
            if len(result)==k: 
                return result