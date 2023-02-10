# %%
from typing import List
import numpy as np


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not np.any(grid) or np.all(grid):
            return -1

        distance = np.array(grid) - 1

        prolife_value = 0
        while (distance < 0).any():
            seed_cord = np.where(distance >= prolife_value)
            temp_cord = []

            for cord in zip(seed_cord[0], seed_cord[1]):
                print(cord, cord[0] - 1 > 0, distance[cord[0] - 1, cord[1]])
                if cord[0] - 1 >= 0 and distance[cord[0] - 1, cord[1]] < 0:
                    temp_cord.append((cord[0] - 1, cord[1]))

                if (
                    cord[0] + 1 < distance.shape[0]
                    and distance[cord[0] + 1, cord[1]] < 0
                ):
                    temp_cord.append((cord[0] + 1, cord[1]))

                if cord[1] - 1 >= 0 and distance[cord[0], cord[1] - 1] < 0:
                    temp_cord.append((cord[0], cord[1] - 1))

                if (
                    cord[1] + 1 < distance.shape[0]
                    and distance[cord[0], cord[1] + 1] < 0
                ):
                    temp_cord.append((cord[0], cord[1] + 1))

            temp_cord = set(temp_cord)
            prolife_cord = [[], []]
            for cord in temp_cord:
                prolife_cord[0].append(cord[0])
                prolife_cord[1].append(cord[1])

            prolife_value += 1
            distance[prolife_cord] = prolife_value

        return distance.max()


# Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
# Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
# Solution().maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
Solution().maxDistance(
    [
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
    ]
)

# %%
