class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker={}
        box=[[]for i in range(len(nums)+1)]
        for i in range(len(nums)): 
            tracker[nums[i]]=1+tracker.get(nums[i],0)
        for n, c in tracker.items():
            box[c].append(n)
        res=[]
        for i in range(len(box)-1,0,-1):
            for num in box[i]:
                res.append(num)
            if len(res)==k:
                return res            
