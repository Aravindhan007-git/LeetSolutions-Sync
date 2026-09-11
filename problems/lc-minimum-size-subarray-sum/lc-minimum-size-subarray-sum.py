class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        size = float('inf')
        n = len(nums)
        c_s = 0
        for right in range(n):
            c_s += nums[right]
            while c_s >= target:
                size = min(size,right - left +1 )
                c_s-=nums[left]
                left+=1
        if size != float('inf'):
            return size
        else:
            return 0
