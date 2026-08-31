class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        c_s=ma=sum(nums[:k])
        
        for i in range(k,len(nums)):
            c_s+=nums[i]-nums[i-k]
            ma=max(ma,c_s)
        return ma/k