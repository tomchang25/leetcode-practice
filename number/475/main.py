# %%
## 475. Heaters

## author: Greysuki
## ref: https://leetcode.com/problems/heaters/discuss/1674672/Python-two-pointers-simple-solution-with-explanation
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        heater_idx = 0
        temp = []
        for house in houses:
            while heater_idx < (len(heaters) - 1) and abs(heaters[heater_idx] - house) >= abs(
                heaters[heater_idx + 1] - house
            ):
                heater_idx += 1

            temp.append(abs(heaters[heater_idx] - house))

        return max(temp)


sol = Solution()
print(sol.findRadius([1, 2, 3], [2]))
print(sol.findRadius([1, 2, 3, 4], [1, 4]))
print(sol.findRadius([1, 5], [2]))
print(sol.findRadius([1, 50, 99], [2, 98]))
print(sol.findRadius([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 4]))
# %%
