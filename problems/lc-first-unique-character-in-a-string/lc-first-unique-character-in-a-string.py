class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        d={}
        for v in s:
            d[v]=d.get(v,0)+1
        c=False

        for x in d:
            if d.get(x,0)==1:
                return s.index(x)
        return -1