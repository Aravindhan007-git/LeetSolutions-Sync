class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def find(s,op,cl,res):
            if len(s)==n*2:
                res.append(s)
                return
            if op<n:
                find(s+'(',op+1,cl,res)
            if cl<op:
                find(s+')',op,cl+1,res)
        find("",0,0,res)
        return res