# %%
## 605. Can Place Flowers
## author: Greysuki
from typing import Optional, List

# Definition for a binary tree node.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr = "".join(map(str, [0] + flowerbed + [0])).split("1")

        ans = sum([(len(x) - 1) // 2 for x in arr])

        return ans >= n


# Your Solution object will be instantiated and called as such:
obj = Solution()
print(obj.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(obj.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(obj.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1], 2))


# %%
