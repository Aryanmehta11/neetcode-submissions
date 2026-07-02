class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        res=0

        while left<right:
            minHeight=min(heights[left],heights[right])
            distance=right-left
            area=minHeight*distance
            res=max(area,res)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return res            




        