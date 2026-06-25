class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        a=[0]*26
        b=[0]*26
        w=len(s1)
        r=len(s2)
        if w>r:
            return False
        for i in s1:
            a[ord(i)-ord('a')]+=1
        for i in range(r):
            if i<w:
                b[ord(s2[i])-ord('a')]+=1
            else:
                b[ord(s2[i-w])-ord('a')]-=1
                b[ord(s2[i])-ord('a')]+=1
            if a==b:
                return True
        return False