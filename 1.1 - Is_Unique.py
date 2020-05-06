class Solution(object):
    def containsDuplicate(self, nums):
        # BUD improvement
        if len(nums)==len(set(nums)):
            return False;

        # sol.2 - t=O(n);s=O(n) w/ additional data structure (hash)
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            hashset[num] = True
        return False

        """
        # sol.1 - t=O(nlogn);s=O(n) w/o additional data structure
        nums.sort();
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True;
                break;
        return False;
        """