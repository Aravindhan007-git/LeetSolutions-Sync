class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        rev=0
        x=abs(x)
        while x>0:
            d=x%10
            rev=rev*10+d
            x//=10
        rev=rev*sign
        if rev>(2**31)-1 or rev<(-2**31):
            return 0
        else :
            return rev