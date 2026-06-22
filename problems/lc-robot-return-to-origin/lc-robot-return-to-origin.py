class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for i in moves:
            if i=='U':
                x+=1
            elif i=='D':
                x-=1
            elif i=='L':
                y-=1
            elif i=='R':
                y+=1
        if not x and not y :
            return True
        else:
            return False