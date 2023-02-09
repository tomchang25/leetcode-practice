# %%
from typing import List
import string


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0

        ideas.sort()
        storage = dict()
        for i in string.ascii_lowercase:
            storage[i] = []

        for idea in ideas:
            storage[idea[0]] += [idea[1:]]

        for a in string.ascii_lowercase:
            for b in string.ascii_lowercase:
                mutual = set(storage[a]) & set(storage[b])

                ans += (
                    2
                    * (len(storage[a]) - len(mutual))
                    * (len(storage[b]) - len(mutual))
                )

        return int(ans / 2)


Solution().distinctNames(["coffee", "donuts", "time", "toffee"])
