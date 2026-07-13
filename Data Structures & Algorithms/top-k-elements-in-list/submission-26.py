class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker={}
        box=[[]for i in range(len(nums)+1)]
        for n in nums: 
            tracker[n]=1+tracker.get(n,0)
        for n, c in tracker.items(): 
            box[c].append(n)
        result=[]
        for i in range(len(box)-1,0,-1):
            for n in box[i]:
                result.append(n)
            if len(result)==k: 
                return result          
