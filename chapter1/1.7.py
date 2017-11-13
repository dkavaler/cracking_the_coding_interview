TEST_INPUT = [[1, 2, 3, 4],
		      [5, 6, 7, 8],
		      [9, 10, 11, 12],
		      [13, 14, 15, 16]]

CORRECT_RESULT = [[13, 9, 5, 1],
                  [14, 10, 6, 2],
                  [15, 11, 7, 3],
                  [16, 12, 8, 4]]


def check_result(result):
    return all([result[i] == CORRECT_RESULT[i] for i in range(len(result))])


# (0, 0) -> (0, n-1)
# (1, 0) -> (0, n-2)
# (2, 0) -> (0, n-3)
# (3, 0) -> (0, n-4)

# (0, 1) -> (1, n-1)
# (0, 2) -> (2, n-1)
# (0, 3) -> (3, n-1)

# (1, 1) -> (1, n-2)
# (1, 2) -> (2, n-2)
# (1, 3) -> (3, n-2)

# formula: (x1, y1) -> (x2, y2)
# x2 = y1, y2 = n - 1 - x1

# Easy way: use a separate NxN matrix and perform the calculation
# O(N^2) time and O(N^2) additional memory
def rotate_90d(m):
	# For clarity
	N = len(m)
	# Initialize new NxN matrix
	new_m = [[i for i in range(N)] for j in range(N)]
	for i in range(N):
		for j in range(N):
			new_m[j][N - 1 - i] = m[i][j]

	return new_m


# Hard way: in place
# Input:
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
#  [13, 14, 15, 16]]

# Reverse each row
# [[4, 3, 2, 1],
#  [8, 7, 6, 5],
#  [12, 11, 10, 9],
#  [16, 15, 14, 13]]

# Then do a diagonal swap
# (Columns become rows, rows become columns)
# (0, 0) -> (3, 3)
# (0, 1) -> (2, 3)
# (0, 2) -> (1, 3)

# (1, 0) -> (3, 2)
# (1, 1) -> (2, 2)

# (2, 0) -> (3, 1)

# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
# O(N^2) time and O(1) space
def rotate_90d_inplace(m):
	N = len(m)
	# Reverse rows
	for i in range(N):
		for j in range(N // 2):
			swap(i, j, i, N - 1 - j, m)

	# Diagonal swap
	for i in range(N - 1):
		for j in range(N - 1 - i):
			swap(i, j, N - 1 - j, N - 1 - i, m)

	return m


def swap(i1, j1, i2, j2, m):
	tmp = m[i1][j1]
	m[i1][j1] = m[i2][j2]
	m[i2][j2] = tmp 


if __name__ == '__main__':
	result = rotate_90d(TEST_INPUT)
	assert check_result(result)

	result = rotate_90d_inplace(TEST_INPUT)
	assert check_result(result)