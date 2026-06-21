class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x={}
        new=list(set(nums))
        for i in range(len(new)):
            a=nums.count(new[i])
            x[new[i]]=a
        return max(x,key=x.get)