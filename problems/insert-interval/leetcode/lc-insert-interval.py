class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mer=[]
        for inter in intervals:
            s2,e2=inter
            if len(mer)==0:
                mer.append(inter)
            else:
                s1,e1=mer[-1]
                if e1>=s2:
                    mer[-1][1]=max(e1,e2)
                else:
                    mer.append(inter)
        return mer