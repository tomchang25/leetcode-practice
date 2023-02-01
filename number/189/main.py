# %%
## 704. Binary Search
## author: Greysuki

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # print(nums)


sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(sol.rotate([-1, -100, 3, 99], 2))
print(sol.rotate([1], 0))
# %%
