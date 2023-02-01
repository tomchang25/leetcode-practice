# %%
## 283. Move Zeroes
## author: Greysuki

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[:] = nums[:i] + nums[i + 1 :]
                count += 1
                continue

            i += 1

        nums[:] = nums[:] + [0] * count


t = [0, 3, 0, 1, 2, 0, 5, 9, 0, 0]
sol = Solution()
sol.moveZeroes(t)
print(t)
