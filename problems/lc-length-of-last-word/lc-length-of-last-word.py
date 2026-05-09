class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sr=s.split()
        lst_word=sr[len(sr)-1]
        return len(lst_word)
        