class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mer=[]
        intervals.sort()
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