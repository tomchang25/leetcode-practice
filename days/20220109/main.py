# %%
## 1463. Cherry Pickup II
## author: Greysuki

from functools import lru_cache


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions * 4

        R = 0
        L = 0
        current_idx = 0
        for x in instructions:
            if x == "G":
                if current_idx == 0:
                    R += 1
                elif current_idx == 1:
                    L += 1
                elif current_idx == 2:
                    R -= 1
                elif current_idx == 3:
                    L -= 1
            elif x == "R":
                current_idx = (current_idx + 1) % 4
            elif x == "L":
                current_idx = (current_idx - 1) % 4

        return R == 0 and L == 0


# Your Solution object will be instantiated and called as such:
obj = Solution()
obj.isRobotBounded("GGLLGG")
obj.isRobotBounded("GG")
obj.isRobotBounded("GL")


# %%
