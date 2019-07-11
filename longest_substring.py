class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        dup_idx = -1
        substring_len = 0
        tmp_len = 0
        dup_flag = False
        substring = list()
        
        for i in range(str_len):
            substring.append(s[i])
            if (len(substring) != len(set(substring))):
                dup_flag = True
                tmp_len = len(substring) - 1
                dup_idx = substring.index(s[i])
                substring = substring[dup_idx + 1:]
                if tmp_len > substring_len:
                    substring_len = tmp_len
            
            if (len(substring) > substring_len):
                substring_len = len(substring)
        
        if (dup_flag == True):
            #print("dup Flag is True")
            return substring_len
        else:
            return str_len
