class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        x=[]
        c=0
        l=0
        for r in range(len(nums)):
            x=nums[l:r+1]
            while len(list(set(x)))==len(list(set(nums))):
                c+=len(nums)-r
                l+=1
                x=nums[l:r+1]
        return c