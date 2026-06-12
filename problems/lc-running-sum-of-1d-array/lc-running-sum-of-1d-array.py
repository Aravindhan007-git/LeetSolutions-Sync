class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        sum=0
        for i in nums:
            sum+=i
            l.append(sum)
        return l
