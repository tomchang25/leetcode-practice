# %%
## 1074. Number of Submatrices That Sum to Target
## author: Greysuki
## ref: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/2298642/Fully-explained-intuition-4-solutions-or-MUST-READ-or-With-Image
from typing import List
from collections import defaultdict

# class Solution:
#     def numSubmatrixSumTarget(
#         self, matrix: List[List[int]], target: int
#     ) -> int:
#         m = len(matrix)
#         n = len(matrix[0])

#         matrixSum = [[0 for _ in range(n)] for _ in range(m)]
#         ansCount = 0

#         for x1 in range(m):
#             for y1 in range(n):
#                 # Calc matrix x1,y1 sum
#                 if x1 == 0 and y1 == 0:
#                     matrixSum[x1][y1] = matrix[x1][y1]
#                 elif x1 == 0:
#                     matrixSum[x1][y1] = matrixSum[x1][y1 - 1] + matrix[x1][y1]
#                 elif y1 == 0:
#                     matrixSum[x1][y1] = matrixSum[x1 - 1][y1] + matrix[x1][y1]
#                 else:
#                     matrixSum[x1][y1] = (
#                         matrix[x1][y1]
#                         + matrixSum[x1][y1 - 1]
#                         + matrixSum[x1 - 1][y1]
#                         - matrixSum[x1 - 1][y1 - 1]
#                     )

#                 for x2 in range(x1 + 1):
#                     for y2 in range(y1 + 1):

#                         subMatrixSum = (
#                             matrixSum[x1][y1]
#                             - (matrixSum[x1][y2 - 1] if y2 - 1 >= 0 else 0)
#                             - (matrixSum[x2 - 1][y1] if x2 - 1 >= 0 else 0)
#                             + (
#                                 matrixSum[x2 - 1][y2 - 1]
#                                 if y2 - 1 >= 0 and x2 - 1 >= 0
#                                 else 0
#                             )
#                         )

#                         if subMatrixSum == target:
#                             ansCount += 1

#         return ansCount


class Solution:
    def numSubmatrixSumTarget(
        self, matrix: List[List[int]], target: int
    ) -> int:
        m = len(matrix)
        n = len(matrix[0])

        matrixSum = [[0 for _ in range(n)] for _ in range(m)]
        ansCount = 0

        for x1 in range(m):
            for y1 in range(n):
                # Calc matrix x1,y1 sum
                if x1 == 0 and y1 == 0:
                    matrixSum[x1][y1] = matrix[x1][y1]
                elif x1 == 0:
                    matrixSum[x1][y1] = matrixSum[x1][y1 - 1] + matrix[x1][y1]
                elif y1 == 0:
                    matrixSum[x1][y1] = matrixSum[x1 - 1][y1] + matrix[x1][y1]
                else:
                    matrixSum[x1][y1] = (
                        matrix[x1][y1]
                        + matrixSum[x1][y1 - 1]
                        + matrixSum[x1 - 1][y1]
                        - matrixSum[x1 - 1][y1 - 1]
                    )

        for x1 in range(m):
            for x2 in range(x1, m):
                # Reduce the problem to subarray sum of target
                subMatrixSum = defaultdict(int)
                subMatrixSum[0] = 1

                for y in range(n):
                    sum = matrixSum[x2][y]

                    if x1 > 0:
                        sum -= matrixSum[x1 - 1][y]

                    if sum - target in subMatrixSum:
                        ansCount += subMatrixSum[sum - target]

                    subMatrixSum[sum] += 1

        return ansCount


sol = Solution()
print(sol.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
print(sol.numSubmatrixSumTarget([[1, -1], [-1, 1]], 0))
print(sol.numSubmatrixSumTarget([[904]], 0))

# %%
