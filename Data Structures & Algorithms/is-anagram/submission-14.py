class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        boxS, boxT = {}, {}
        for i in range(len(s)): 
            boxS[s[i]]=1+boxS.get(s[i],0)
            boxT[t[i]]=1+boxT.get(t[i],0)
        for c in boxS: 
            if boxS[c] !=boxT.get(c,0):
                return False
        return True
