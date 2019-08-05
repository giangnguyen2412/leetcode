from itertools import permutations, groupby
class Solution(object):
    def threeSumBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        permut = list(permutations(nums, 3))
        match_trip = []
        match_trip_set = []
        
        
        for triplet in permut:
            if (sum(triplet) == 0):
                match_trip.append(triplet)
  
        for triplet in match_trip:
            triplet_list = list(triplet)
            triplet_list.sort()
            match_trip_set.append(triplet_list)
            
        match_trip_set.sort()
        ret = list(match_trip_set for match_trip_set,_ in itertools.groupby(match_trip_set))
                
        return ret
    
    # Use two hash table to perform 3sum and 2sum
    def threeSumNaiveHash(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dct = {}
    
        triplet = []
        nums_len = len(nums)
        for i in range(nums_len):
            value1 = 0 - nums[i]
            for j in range(i + 1, nums_len):
                value2 = value1 - nums[j]
                if (value2 in nums[j+1:]):
                    candidate = [nums[i], nums[j], value2]
                    candidate.sort()
                    key = str(candidate[0]) +  str(candidate[1]) + str(candidate[2])
                    if (key not in dct):
                        dct[key] = True
                        triplet.append(candidate)

        return triplet
                    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dct = {}
        trip = {}
        triplet = []
        
        
        nums_len = len(nums)
        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                key = nums[i] + nums[j]
                if key in dct:
                    dct[key] = dct[key] + [i, j]  # If exists, append more in a bucket
                else:
                    dct[key] = [i, j]
                    
        for k in range(nums_len):
            supplement = -1*nums[k]  # nums[k] = - (nums[i] + num[j])
            if supplement in dct:
                entry = dct[supplement]  #look on the dict
                entry_len = len(entry)
                entry_num = entry_len//2
                for m in range(entry_num):
                    pair = [entry[m*2], entry[m*2+1]]
                    if (k not in pair):
                        candidate = [nums[entry[m*2]], nums[entry[m*2+1]], nums[k]]
                        candidate.sort()
                        key = str(candidate[0]) +  str(candidate[1]) + str(candidate[2])
                        if (key not in trip):
                            trip[key] = True
                            triplet.append(candidate)
                        
        return triplet
                
