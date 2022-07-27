class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k == len(num)):
            return '0'
        stack = deque()
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        while(k):
            stack.pop()
            k -= 1
        s = ''
        for n in stack:
            s += n
        return str(int(s))          
