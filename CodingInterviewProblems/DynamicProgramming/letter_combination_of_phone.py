class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d_to_s = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                  '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        chosen = ""
        result = []
        self._letterCombinations(digits, d_to_s, chosen, len(digits), result)
        return result

    def _letterCombinations(self, digits, d_to_s, chosen, k, result):
        if k == 0:
            # Base case
            result.append(chosen)
            print(chosen)
        else:
            for i in range(len(digits)):
                for c in d_to_s[digits[i]]:
                    chosen = chosen + c
                    self._letterCombinations(digits[i + 1:], d_to_s, chosen, k-1,
                                             result)
                    chosen = chosen[:-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations('23'))
