# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        """Solution 3
        Start from the top, and only move left and down
        """
        rows, cols = binaryMatrix.dimensions()
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 0:
                row += 1
            else:
                col -= 1

        return col + 1 if col != cols - 1 else -1

    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        """Draft 1
        Divide and conquer solution. And try to eliminate rows while working through it
        Beat 59%
        This is basically an optimized version of solution 2
        """
        dim = binaryMatrix.dimensions()
        rows = range(0, dim[0])
        cols = range(0, dim[1])
        return self.helper(binaryMatrix, rows, cols)

    def helper(self, binaryMatrix: "BinaryMatrix", rows, cols) -> int:
        if not rows or not cols:
            return -1

        # Divide and Conquer
        mid_col_index = len(cols) // 2
        col = cols[mid_col_index]
        rows_to_remove = set()
        for row in rows:
            if binaryMatrix.get(row, col) == 0:
                rows_to_remove.add(row)

        if len(rows_to_remove) < len(rows):
            # This col has 1
            if len(cols) == 1:
                return col

            rows = [row for row in rows if row not in rows_to_remove]
            previous_matrix_res = self.helper(binaryMatrix, rows, cols[:mid_col_index])
            if previous_matrix_res >= 0:
                return previous_matrix_res
            else:
                return col
        else:
            # This col has all 0
            return self.helper(binaryMatrix, rows, cols[mid_col_index + 1 :])
