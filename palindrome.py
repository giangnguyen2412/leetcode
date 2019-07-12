class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        string_len = len(s)
        
        max_len = 0
        tmp_len = 0
        
        for i in range(1, string_len):
            
            # Early stop if the current longest palindrome is bigger than the remaining
            if (max_len > (string_len - 1 -i)*2 + 1):
                break
            
            for j in range(1, i+1):
            # We expand to 2 directions, when one direction touches the boundary, stop looping
                if((i - j < 0) or (i + j > string_len)):
                    break
                
                # The case left -> right AND left = reverse(right)
                if (s[i-j:i] == (s[i+1:i+1+j])[::-1]):
                    tmp_string = s[i-j:i+1+j]
                    tmp_len = 2*j + 1
                    
                # The case left -> an element -> right AND left = reverse(right)
                elif (s[i-j:i] == (s[i:i+j])[::-1]):
                    tmp_string = s[i-j:i+j]
                    tmp_len = 2*j
                else:
                    break
                
                if (tmp_len > max_len):
                    max_len = tmp_len
                    max_string = tmp_string
                j += 1
                    
        if (string_len == 0): # While input is an empty string
            return ''
        elif (max_len):
            return max_string
        else:
            return s[0] # While input is a set string, return an ambiguous letter
            
    
