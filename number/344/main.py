# %%
## 344. Reverse String
## author: Greysuki

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


t = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverseString(t)
print(t)

# %%
