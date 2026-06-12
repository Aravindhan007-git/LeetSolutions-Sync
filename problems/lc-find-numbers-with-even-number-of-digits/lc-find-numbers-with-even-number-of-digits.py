class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            x=0
            while i>0:
                i=i//10
                x+=1
            if x%2==0:
                c+=1
        return c
