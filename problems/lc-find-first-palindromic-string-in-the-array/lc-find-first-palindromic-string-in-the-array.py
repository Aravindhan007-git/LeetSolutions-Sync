class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=0
        for i in words:
            if i==i[::-1]:
                f=1
                return i
        if not f:
            return ""
