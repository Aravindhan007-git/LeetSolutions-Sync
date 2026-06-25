class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl=len(s)
        pl=len(p)
        if pl>sl:
            return []
        a=[0]*26
        b=[0]*26
        x=[]
        for i in p:
            b[ord(i)-ord('a')]+=1
        for i in range(sl):
            a[ord(s[i])-ord('a')]+=1
            if i>=pl:
                a[ord(s[i-pl])-ord('a')]-=1
            if i>=pl-1 and  a==b:
                x.append(i-pl+1)
        return x