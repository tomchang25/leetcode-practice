# %%
## 1463. Cherry Pickup II
## author: Greysuki

from functools import lru_cache


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return "{0:b}".format(a + b)


# Your Solution object will be instantiated and called as such:
obj = Solution()
print(obj.addBinary(a="1010", b="1011"))
print(obj.addBinary(a="11", b="1"))
print(obj.addBinary(a="1", b="11"))
print(obj.addBinary(a="1", b="1111111111111101"))

# %%
