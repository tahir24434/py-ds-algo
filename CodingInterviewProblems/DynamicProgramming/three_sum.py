"""
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        chosen = []
        result = list()
        self._threeSum(nums, chosen, 3, result)
        print(result)
        return result

    def is_zero_sum(self, chosen):
        sum = 0
        for num in chosen:
            sum += num
        return sum == 0

    def _threeSum(self, nums, chosen, k, result):
        if k == 0:
            if self.is_zero_sum(chosen):
                result.append([chosen[0], chosen[1], chosen[2]])
        else:
            for i in range(len(nums)):
                chosen.append(nums[i])
                self._threeSum(nums[i + 1:], chosen, k - 1, result)
                chosen.pop()


if __name__ == "__main__":
    A = [-1, 0, 1]
    sol = Solution()
    print(sol.threeSum(A))
