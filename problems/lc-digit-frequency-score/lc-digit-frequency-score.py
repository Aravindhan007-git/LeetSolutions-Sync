class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        n = list(str(n))
        d = {}
        for v in n:
            d[v] = d.get(v,0)+1

        l = list(d.items())
        for v in l:
            x,y = v
            score += (int(x)*y)
        return score