class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums=[[0]*n for _ in range(n)]
        top=0
        left=0
        bottom=n-1
        right=n-1
        a=1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                nums[top][i]=a
                a+=1
            top+=1
            for i in range(top,bottom+1):
                nums[i][right]=a
                a+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    nums[bottom][i]=a
                    a+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    nums[i][left]=a
                    a+=1
                left+=1
        return nums