# %%
## 1009. Complement of Base 10 Integer
## author: Greysuki

from typing import List
import math


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        if math.log2(n).is_integer():
            return n - 1

        return pow(2, math.ceil(math.log2(n))) - 1 - n




sol = Solution()
print(sol.bitwiseComplement(0))
print(sol.bitwiseComplement(1))
print(sol.bitwiseComplement(2))
print(sol.bitwiseComplement(3))
print(sol.bitwiseComplement(4))
print(sol.bitwiseComplement(5))
print(sol.bitwiseComplement(7))
print(sol.bitwiseComplement(10))
print(sol.bitwiseComplement(16))

# %%
