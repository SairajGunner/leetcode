# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set({})
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return True
        return False
