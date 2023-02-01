# %%
## 35. Search Insert Position
## author: Greysuki

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0

        return self.helper(nums, target, 0, len(nums))

    def helper(self, nums, target, l, r):
        print(l, r)
        if r - l == 1:
            return l if target <= nums[l] else r

        mid = (l + r) // 2

        if target < nums[mid]:
            return self.helper(nums, target, l, mid)
        else:
            return self.helper(nums, target, mid, r)


sol = Solution()
print(sol.searchInsert([1, 3], 5))
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2))
print(sol.searchInsert([1, 3, 5, 6], 7))
print(sol.searchInsert([1, 3, 5, 6], 9))

# %%
