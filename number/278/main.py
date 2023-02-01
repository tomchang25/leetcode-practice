# %%
## 278. First Bad Version
## author: Greysuki

from typing import List


def isBadVersion():
    pass


class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1

        return self.helper(1, n)

    def helper(self, l, r):
        if r - l == 1:
            return r

        mid = (l + r) // 2
        if isBadVersion(mid):
            return self.helper(l, mid)
        else:
            return self.helper(mid, r)


# sol = Solution()
# print(sol.search([-1, 0, 3, 5, 9, 12], 9))
# print(sol.search([-1, 0, 3, 5, 9, 12], 4))
# print(sol.search([-1, 0, 3, 5, 9, 12], -1))
# print(sol.search([-1, 0, 3, 5, 9, 12], 12))

# %%
