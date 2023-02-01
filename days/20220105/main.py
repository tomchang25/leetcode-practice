# %%
## 131. Palindrome Partitioning
## author: Greysuki

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.rec([], [], s)

    # private
    def isPalindrom(self, s):
        return s == s[::-1]

    def rec(self, result, pre, s):
        # print(pre, s)

        if len(s) == 0:
            result.append(pre)
            return pre

        for i in range(0, len(s)):
            if self.isPalindrom(s[: i + 1]):
                self.rec(result, pre + [s[: i + 1]], s[i + 1 :])

        return result


sol = Solution()
print(sol.partition("xxyy"))
print(sol.partition("aab"))
print(sol.partition("a"))

# %%
