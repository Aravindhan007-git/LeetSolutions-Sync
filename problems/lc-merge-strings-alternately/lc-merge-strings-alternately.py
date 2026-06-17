class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        i=j=0
        s=''
        while i<len(word1) and j<len(word2):
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        if j==len(word2):
            while i<len(word1):
                s+=word1[i]
                i+=1
        else:
            while j<len(word2):
                s+=word2[j]
                j+=1
        return s