# %%
## 1094. Car Pooling
## author: Greysuki

from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        priority_heap = []
        for numPassengers, f, t in trips:
            # print(numPassengers, f, t)
            heapq.heappush(priority_heap, (f, numPassengers))
            heapq.heappush(priority_heap, (t, -numPassengers))

        current_cap = 0
        while len(priority_heap) > 0:
            current_cap += heapq.heappop(priority_heap)[1]
            if current_cap > capacity:
                return False

        return True


sol = Solution()
print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 4))
print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 5))
print(sol.carPooling([[2, 4, 5], [3, 2, 7]], 4))
print(sol.carPooling([[2, 4, 5], [3, 2, 7]], 5))

# %%
