# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/

# This solution can be done using a list directly
# However, I observed that there is a good performance improvement with hash_set
# The testcase took 31ms to complete with list and only 22ms with set

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = set()
        for num in nums1:
            if num in nums2:
                if num in intersection:
                    continue
                else:
                    intersection.add(num)
        
        return list(intersection)