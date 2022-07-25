class Solution:
    def reverseWords(self, s: str) -> str:
        buffer = []
        
        reversedSentence = ''
        for c in s:
            if c != ' ':
                buffer.append(c)
            elif c == ' ' and buffer:
                reversedSentence = ''.join(buffer) + ' ' + reversedSentence
                buffer = []
                print(reversedSentence)
                
        if buffer:
            reversedSentence = ''.join(buffer) + ' ' + reversedSentence
            
        return reversedSentence[:-1]
