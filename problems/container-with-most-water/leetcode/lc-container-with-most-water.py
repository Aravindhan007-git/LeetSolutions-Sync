class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l=len(height)-1
        s=0
        while s<l:
            width=l-s
            m=min(height[l],height[s])*width
            if m>max_area:
                max_area=m
            if height[s]<height[l]:
                s+=1
            else:
                l-=1 
        return max_area