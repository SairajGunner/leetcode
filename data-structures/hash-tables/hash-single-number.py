class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            else:
                hash_set.add(num)
        
        return hash_set.pop()