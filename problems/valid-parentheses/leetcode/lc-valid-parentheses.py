class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for v in s:
            if v=='(' or v=='{' or v=='[':
                st.append(v)
            else:
                if not st:
                    return False
                top=st.pop()
                if v==')' and top!='(':
                    return False
                elif v=='}' and top!='{':
                    return False
                elif v==']' and top!='[':
                    return False
        return len(st)==0