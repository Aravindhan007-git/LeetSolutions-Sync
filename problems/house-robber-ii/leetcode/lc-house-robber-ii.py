class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n<=2:
            return max(nums)
        dpf = [0]*n
        dpf[1] = nums[1]
        for i in range(2,n):
            dpf[i] = max(dpf[i-1],nums[i]+dpf[i-2])
        
        dpl = [0]*n
        dpl[0] = nums[0]
        dpl[1] = max(nums[0],nums[1])
        for i in range(2,n-1):
            dpl[i] = max(dpl[i-1],nums[i]+dpl[i-2])

        for v in dpl:
            dpf.append(v)

        return max(dpf)