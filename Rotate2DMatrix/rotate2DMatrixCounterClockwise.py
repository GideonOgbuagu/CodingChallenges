# Do not return anything, modify matrix in-place instead.
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (counter-clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation

def rotateCounterClockwise(matrix):

    # transpose: swap columns for rows
    for i in range(len(matrix)):
        j = i
        while j < len(matrix):
            # swap column and row values excluding the diagonals
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            j += 1

    # reverse all rows in matrix
    matrix.reverse()


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7],
]

print(f'before counter-clockwise rotation:')
for row in matrix:
    print(f'{row}')

rotateCounterClockwise(matrix)
print(f'\nafter counter-clockwise rotation:')
for row in matrix:
    print(f'{row}')

# Expected output:

# [4, 8, 3, 7]
# [3, 7, 2, 6]
# [2, 6, 1, 5]
# [1, 5, 9, 4]
