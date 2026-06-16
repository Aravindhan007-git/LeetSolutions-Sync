class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['A','E','I','O','U','a','e','i','o','u']
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i] not in v:
                i+=1
                continue
            elif s[j] not in v:
                j-=1
                continue
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)
