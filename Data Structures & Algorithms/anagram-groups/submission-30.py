class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs: 
            box=[0]*26
            for c in s: 
                box[(ord(c)-ord("a"))]+=1
            result[tuple(box)].append(s)
        return list(result.values())
        