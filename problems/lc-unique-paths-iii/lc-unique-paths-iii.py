class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x=len(grid)
        y=len(grid[0])
        sol=[[0]*y for _ in range(x)]
        self.w=0
        def path(i,j):
            if i<0 or j<0 or i>=x or j>=y or grid[i][j]==-1 or sol[i][j]==1 :
                return
            if grid[i][j]==2:
                sol[i][j]=1
                t=1
                for a in range(x):
                    for b in range(y):
                        if sol[a][b]==0 and grid[a][b]!=-1:
                            t=0
                if t==1:
                    self.w+=1
                sol[i][j]=0
                return
            sol[i][j]=1
            path(i+1,j)
            path(i,j+1)
            path(i-1,j)
            path(i,j-1)
            sol[i][j]=0
            return
        for a in range(x):
            for b in range(y):
                if grid[a][b]==1:
                    path(a,b)
                    return self.w