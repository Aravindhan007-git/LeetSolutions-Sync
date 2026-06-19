class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=len(words)
        x=[]
        for i in range(l):
            for j in range(l):
                if words[i] in words[j] and i!=j and words[i] not in x:
                    x.append(words[i])
        return x