class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=sorted(set(nums),reverse=True)
        if len(x)>=3:
            return x[2]
        else:
            return x[0]