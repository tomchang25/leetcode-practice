# %%
## 704. Binary Search
## author: Greysuki

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums))

    def helper(self, nums, target, l, r):
        # print(l, r)
        if l == r:
            return -1

        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            return self.helper(nums, target, l, mid)
        else:
            return self.helper(nums, target, mid + 1, r)


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))
print(sol.search([-1, 0, 3, 5, 9, 12], 4))
print(sol.search([-1, 0, 3, 5, 9, 12], -1))
print(sol.search([-1, 0, 3, 5, 9, 12], 12))

# %%
