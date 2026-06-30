class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums,low,high):
            if low<high:
                mid=(low+high)//2
                mergesort(nums,low,mid)
                mergesort(nums,mid+1,high)
                merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            left=nums[low:mid+1]
            right=nums[mid+1:high+1]
            i=j=0
            k=low
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            return nums
        mergesort(nums,0,len(nums)-1)
        return nums