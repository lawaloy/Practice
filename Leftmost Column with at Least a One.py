/*
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly
*/

# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation

Constraints:

#rows == mat.length
#cols == mat[i].length
#1 <= rows, cols <= 100
#mat[i][j] is either 0 or 1.
#mat[i] is sorted in a non-decreasing way.

#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
        
#         current_row = 0
#         current_col = cols - 1
#         while current_row < rows and current_col >= 0:
#             if binaryMatrix.get(current_row, current_col) == 0:
#                 current_row += 1
#             else:
#                 current_col -= 1
#         if current_col != cols - 1:
#             return current_col + 1
#         else:
#             return -1

#OR
        
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()
        
        r, c = 0, N - 1 
        leftmost_col = -1
        while r < M and c >= 0:
            if binaryMatrix.get(r,c) == 1:
                leftmost_col = c
                c -= 1
            else:
                r += 1
        return leftmost_col

    
