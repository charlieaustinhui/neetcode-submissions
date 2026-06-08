class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        rules={"}":"{", ")":"(", "]":"["}
        
        for char in s: 
                if char in rules:
                        if stack and stack[-1]==rules[char]:
                                stack.pop()
                        else: 
                                return False
                else: 
                        stack.append(char)
        if not stack: 
                return True
        else: 
                return False