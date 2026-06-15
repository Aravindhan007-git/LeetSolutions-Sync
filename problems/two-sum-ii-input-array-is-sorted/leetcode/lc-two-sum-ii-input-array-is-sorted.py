class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=0
        l=len(numbers)-1
        while s<l:
            sum=numbers[s]+numbers[l]
            if sum==target:
                return [s+1,l+1]
            elif sum<target:
                s+=1
            else:
                l-=1
        return []