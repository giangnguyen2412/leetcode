class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        dct = {}
        
        i = j = 0
        n = len(s)
        
        while (i < n) and (j < n):
            if s[j] not in dct:
                dct[s[j]] = 1 # dummy value, just care the key
                j += 1
                max_len = max(max_len, j - i)
            else:
                del dct[s[i]]
                i += 1
        
        return max_len
