class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        chosen = list()
        self._twoSum(nums, target, chosen, len(nums))
        return chosen

    def _twoSum(self, nums, target, chosen, m):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target == 0:
            print(chosen)
            return True
        if m == 0:
            return False

        chosen.append(nums[m - 1])
        withi = self._twoSum(nums, target - nums[m-1], chosen,
                            m - 1)
        chosen.pop()
        without = self._twoSum(nums, target, chosen, m - 1)
        return withi or without

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,4]
    target = 6
    s.twoSum(nums, target)