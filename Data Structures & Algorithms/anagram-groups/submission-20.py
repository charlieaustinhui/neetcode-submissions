class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs: 
            address=[0]*26
            for c in s: 
                address[ord(c)-ord("a")]+=1
            result[tuple(address)].append(s)
        return list(result.values())