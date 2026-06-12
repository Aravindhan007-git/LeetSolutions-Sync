class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        w=0
        for i in accounts:
            w=max(w,sum(i))
        return w  
