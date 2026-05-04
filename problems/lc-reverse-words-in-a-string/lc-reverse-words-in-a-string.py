class Solution:
    def reverseWords(self, s: str) -> str:
        sp=s.split()
        clean=" ".join(sp)
        rev=clean.split()[::-1]
        fin=" ".join(rev)
        return fin