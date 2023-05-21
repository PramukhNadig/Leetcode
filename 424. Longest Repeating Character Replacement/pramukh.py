class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {}
        maxF = 0
        m = 0
        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
            maxF = max(maxF, chars[s[i]])

            if(maxF + k < i - l + 1):
                chars[s[l]] -= 1
                l += 1
            m = max(m, i - l + 1)
        return m
      
      #notes
      #no need to update maxF because it should be updating only when we find a better solution
      #
