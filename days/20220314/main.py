# %%
## 71. Simplify Path
## author: Greysuki


# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         path_stack = []
#         while len(path) > 0:
#             # print(path, path_stack, path.find("/"))
#             if path[0] == "/":
#                 path = path[1:]
#             elif path[0] == "." and (len(path) == 1 or path[1] == "/"):
#                 path = path[1:]
#             elif path[0:2] == ".." and (len(path) == 2 or path[2] == "/"):
#                 path = path[2:]
#                 if len(path_stack) > 0:
#                     path_stack.pop()
#             else:
#                 key = path.find("/")
#                 if key == -1:
#                     path_stack.append(path)
#                     path = ""
#                 else:
#                     path_stack.append(path[:key])
#                     path = path[key:]

#         return "/" + "/".join(path_stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        for f in path.split("/"):
            if f == "..":
                if path_stack:
                    path_stack.pop()
            elif f == "." or not f:
                continue
            else:
                path_stack.append(f)

        return "/" + "/".join(path_stack)


# Your Solution object will be instantiated and called as such:
obj = Solution()
print(obj.simplifyPath("/..hidden"))
print(obj.simplifyPath("/.../"))
print(obj.simplifyPath("/../"))
print(obj.simplifyPath("/13/11/////.././22/111/../"))
