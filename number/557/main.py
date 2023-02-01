# %%
## 344. Reverse String
## author: Greysuki

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()

        for k, x in enumerate(sl):
            sl[k] = sl[k][::-1]

        return " ".join(sl)


t = "Let's take LeetCode contest"
sol = Solution()
a = sol.reverseWords(t)
print(a)

# %%
