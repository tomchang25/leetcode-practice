# %%
## 1094. Car Pooling
## author: Greysuki
## Ref: https://florian.github.io/reservoir-sampling/

from typing import List, Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        pass

    def getRandom(self) -> int:
        node = self.head

        v = None
        count = 1
        while node is not None:
            if random.random() < (1 / count):
                v = node.val

            node = node.next
            count += 1

        return v


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


a = ListNode(1)

b = ListNode(2)
a.next = b

c = ListNode(3)
b.next = c

d = ListNode(4)
c.next = d

head = a

obj = Solution(head)
param_1 = obj.getRandom()
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())

# %%
