class Solution(object):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    def twoSum(self, nums, target):
        hashMap = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[j] = i
