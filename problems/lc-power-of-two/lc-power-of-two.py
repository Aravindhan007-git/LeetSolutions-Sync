class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while 1:
            if 2**i==n:
                return True
            if 2**i>n:
                return False
            i+=1