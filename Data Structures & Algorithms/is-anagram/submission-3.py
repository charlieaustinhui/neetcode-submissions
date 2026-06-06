class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        box = {}
        for n in s: 
            box[n] = box.get(n, 0) + 1
        for y in t:
            if y in box:
                box[y] -= 1
                if box[y] == 0:
                    del box[y]
        if not box:
            return True
        return False