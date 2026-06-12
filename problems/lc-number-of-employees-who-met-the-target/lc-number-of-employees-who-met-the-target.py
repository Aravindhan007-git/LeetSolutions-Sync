class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        g=0
        for i in hours:
            if i>=target:
                g+=1
        return g