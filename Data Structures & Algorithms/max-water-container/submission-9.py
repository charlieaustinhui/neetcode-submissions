class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        leftPointer, rightPointer= 0,len(heights)-1

        while(leftPointer<rightPointer):
                area=min(heights[leftPointer], heights[rightPointer])*(rightPointer-leftPointer)
                maxArea=max(area,maxArea)
                if(heights[leftPointer]<heights[rightPointer]):
                        leftPointer+=1
                else: 
                        rightPointer-=1
        return maxArea
