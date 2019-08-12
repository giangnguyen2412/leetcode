class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        str_len = len(s)
        s_dct = {}
        t_dct = {}
        
        s_set = []
        t_set = []
        
        for i in range(str_len):
            if (s[i] not in s_set):
                s_set.append(s[i])
                
            if (t[i] not in t_set):
                t_set.append(t[i])
                
            if (s[i] not in s_dct):
                s_dct[s[i]] = str(i)
            else:
                s_dct[s[i]] += str(i)
        
            if (t[i] not in t_dct):
                t_dct[t[i]] = str(i)
            else:
                t_dct[t[i]] += str(i)
            
        s_set_len = len(s_set)
        t_set_len = len(t_set)
        
        if (s_set_len != t_set_len):
            return False
        
        for i in range(s_set_len):
            s_c = s_set[i]
            t_c = t_set[i]
            if (s_dct[s_c] != t_dct[t_c]):
                return False
        
        return True
