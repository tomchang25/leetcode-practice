# %%
## 1463. Cherry Pickup II
## author: Greysuki

from typing import List
from functools import lru_cache

import numpy as np


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.cache = -np.ones(
            (len(self.grid), len(self.grid[0]), len(self.grid[0]))
        ).astype(int)

        return self.helper(0, 0, len(self.grid[0]) - 1)

    @lru_cache(None)
    def helper(self, row, coli, colj):
        if row == len(self.grid):
            return 0

        if self.cache[row, coli, colj] > 0:
            return self.cache[row, coli, colj]

        temp = []
        for i in range(-1, 2):
            if coli + i < 0 or coli + i >= len(self.grid[0]):
                continue
            for j in range(-1, 2):
                if colj + j < 0 or colj + j >= len(self.grid[0]):
                    continue

                grid_temp = 0
                if coli != colj:
                    grid_temp = self.grid[row][coli] + self.grid[row][colj]
                else:
                    grid_temp = self.grid[row][coli]

                grid_temp += self.helper(row + 1, coli + i, colj + j)
                temp.append(grid_temp)

        self.cache[row, coli, colj] = max(temp)

        print(row, coli, colj, self.cache[row, coli, colj])
        return self.cache[row, coli, colj]


# Your Solution object will be instantiated and called as such:
obj = Solution()
param_1 = obj.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])

print(param_1)

param_2 = obj.cherryPickup(
    [
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6],
    ]
)

print(param_2)

# %%
temp = [
    1,
    3,
    5,
    8,
]
print(max(temp))
