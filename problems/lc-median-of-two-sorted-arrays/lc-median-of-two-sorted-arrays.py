class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1,nums2):
            i=j=0
            x=[]
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    x.append(nums1[i])
                    i+=1
                else:
                    x.append(nums2[j])
                    j+=1
            while i<len(nums1):
                x.append(nums1[i])
                i+=1
            while j<len(nums2):
                x.append(nums2[j])
                j+=1
            return x
        mer=merge(nums1,nums2)
        i,j=0,len(mer)-1
        while i<j:
            i+=1
            j-=1
        return (mer[i]+mer[j])/2