class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box=set()
        mx=0
        l=0
        for r in range(len(s)):
                while s[r] in box: 
                        box.remove(s[l])
                        l+=1
                box.add(s[r])
                mx=max(r-l+1,mx)
        return mx