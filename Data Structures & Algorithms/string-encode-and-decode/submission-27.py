class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs: 
            result+=str(len(word))+"#"+word
        return result

    def decode(self, encode:str):
        end=[]
        i=0
        while i<len(encode): 
            j=i
            while encode[j]!="#":
                j+=1
            length=int(encode[i:j])
            end.append(encode[j+1:j+1+length])
            i=j+1+length
        return end  
