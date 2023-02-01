# %%
## 605. Can Place Flowers
## author: Greysuki

from typing import Optional, List
from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list_str = f"{self.val}, "

        node = self.next
        while node is not None:
            list_str += f"{node.val}, "
            node = node.next

        return list_str


def CreateList(arr: Optional[List]):
    arr.reverse()
    pre_node = None
    for val in arr:
        node = ListNode(val)
        if pre_node is not None:
            node.next = pre_node

        pre_node = node

    return pre_node


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        list1 = deepcopy(list1)
        list2 = deepcopy(list2)
        cur = ListNode()
        root = cur
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        while list1 is not None:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

        while list2 is not None:
            cur.next = list2
            cur = cur.next
            list2 = list2.next

        return root.next


# Your Solution object will be instantiated and called as such:
obj = Solution()
a = CreateList([1, 1, 3, 4, 5, 5, 7, 8, 11])
b = CreateList([1, 2, 2, 2, 6])
print(obj.mergeTwoLists(a, b))
print(a)
print(b)

# %%
b = ListNode(2)
a = ListNode(1, b)


print(a)

# %%

# %%
