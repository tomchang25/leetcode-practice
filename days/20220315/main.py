# %%
## 1249. Minimum Remove to Make Valid Parentheses
## author: Greysuki
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        c = 0
        stack = []
        split_s = list(s)
        while c < len(split_s):
            if split_s[c] == "(":
                stack.append(c)
            elif split_s[c] == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    split_s[c] = ""
            c += 1

        while stack:
            split_s[stack.pop()] = ""

        return "".join(split_s)


# Your Solution object will be instantiated and called as such:
obj = Solution()
print(obj.minRemoveToMakeValid("lee(t(c)o)de)"))
