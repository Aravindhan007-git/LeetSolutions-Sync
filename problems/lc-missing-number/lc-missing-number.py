class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mis=0
        for i in range(len(nums)+1):
            mis^=i
        for i in nums:
            mis^=i

        return mis