class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len -1):
            value1 = nums[i]
            value2 = target - value1
            for j in range(i+1, nums_len):
                if (nums[j] == value2):
                    return [i,j]
            
        return []
    
    """
    Time complexity: O(n) because we need to loop over nums, hashing takes O(1)
    Space complexity: O(n)
    """
    def twoSum_hash1(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]
            
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
        
