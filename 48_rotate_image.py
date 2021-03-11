from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Solution 3
        [MEMO+1] Optimized version of draft 1 to do rotation of 4 points in single loop
        There is also solution 1 which takes mathematical approach
        """
        N = len(matrix)
        for i in range(N // 2 + N % 2):
            for j in range(N // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[N - j - 1][i]
                matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
                matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
                matrix[j][N - i - 1] = tmp
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """Draft 1
        Formula for replacement is (i, j) -> (j, N - i)
        """
        N = len(matrix)
        updated = set()
        for i in range(N):
            for j in range(N):
                if i == 1 and j == 1:
                    pass

                if (i, j) in updated:
                    continue

                val = matrix[i][j]
                curr_i = j
                curr_j = N - i - 1
                while (curr_i, curr_j) not in updated:
                    curr_val = matrix[curr_i][curr_j]
                    matrix[curr_i][curr_j] = val
                    val = curr_val
                    updated.add((curr_i, curr_j))

                    next_i = curr_j
                    next_j = N - curr_i - 1
                    curr_i = next_i
                    curr_j = next_j
