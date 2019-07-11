class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        digit_list = list()
        if (x == 0):
            return x
        sign = x/abs(x)
        x = abs(x)
        ret_val = 0
        upper = 2**31 - 1
        lower = -(2**31)
        
        while (x != 0):
            if (sign == 1):
                if (ret_val > upper/10) or (ret_val == upper/10 and x%10 > 6):
                    return 0
            else:
                if (ret_val > upper/10) or (ret_val == upper/10 and x%10 > 7):
                    return 0
                
            ret_val = ret_val*10 + x%10
            x = x/10
            
        ret_val = sign*ret_val
                    
        return ret_val
        
