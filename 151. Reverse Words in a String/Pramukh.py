class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(' ')
        res = ''
        
        for i in range(len(t)-1, -1, -1):
            if(t[i] == ''):
                continue
            res += t[i].lstrip(' ').rstrip(' ')
            res += ' '
        return res.rstrip()
            
