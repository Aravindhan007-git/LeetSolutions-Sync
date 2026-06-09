class Solution:
    def isPalindrome(self, s: str) -> bool:
        x="".join(ch.lower() for ch in s if ch.isalnum())
        if x==x[::-1]:
            return True
        else:
            return False
