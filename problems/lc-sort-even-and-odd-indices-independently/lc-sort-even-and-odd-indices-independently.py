class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e=sorted(e)
        o=sorted(o,reverse=True)
        y=[]
        for i in range(len(nums)//2):
            y.append(e[i])
            y.append(o[i])
        if len(nums)%2!=0:
            y.append(e[-1])
        return y