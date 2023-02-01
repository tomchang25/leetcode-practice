# %%
## 283. Move Zeroes
## author: Greysuki
## ref: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            temp = target - (numbers[l] + numbers[r])

            if temp > 0:
                l += 1
            elif temp < 0:
                r -= 1
            else:
                return (l + 1, r + 1)

        raise BaseException("Something is wrong")


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([2, 3, 4], 6))
