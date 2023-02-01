# %%
## 704. Binary Search
## author: Greysuki

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negs = []
        poss = []
        result = []
        for x in nums:
            if x < 0:
                negs.append(x ** 2)
            elif x > 0:
                poss.append(x ** 2)
            else:
                result.append(0)

        while 1:
            if len(poss) == 0:
                result += negs[::-1]
                break

            if len(negs) == 0:
                result += poss
                break

            if negs[-1] < poss[0]:
                result.append(negs[-1])
                del negs[-1]
            else:
                result.append(poss[0])
                del poss[0]

        return result


sol = Solution()
print(sol.sortedSquares([-4, -3, -1, 0, 3, 10]))
print(sol.sortedSquares([-5, -3, -2, -1]))
# %%
