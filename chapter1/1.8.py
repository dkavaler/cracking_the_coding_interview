from copy import deepcopy

TEST_INPUT = [[1, 2, 0, 4],
		      [5, 6, 7, 8],
		      [9, 0, 11, 12],
		      [13, 14, 15, 16],
		      [17, 18, 19, 20],
		      [21, 22, 23, 24]]

CORRECT_RESULT = [[0, 0, 0, 0],
			      [5, 0, 0, 8],
                  [0, 0, 0, 0],
                  [13, 0, 0, 16],
                  [17, 0, 0, 20],
                  [21, 0, 0, 24]]


def check_result(result):
    return all([result[i] == CORRECT_RESULT[i] for i in range(len(result))])


# O(M * N) time, but wasteful because we need O(M + N) extra space for
# our zeroed_cols and zeroed_rows
def zero_matrix_extramem(m):
    zeroed_cols, zeroed_rows = [], []
    M = len(m)
    N = len(m[0])

    for i in range(M):
        for j in range(N):
            if m[i][j] == 0:
                zeroed_rows.append(i)
                zeroed_cols.append(j)

    for i in range(M):
        for j in range(N):
            if i in zeroed_rows or j in zeroed_cols:
                m[i][j] = 0

    return m

# O(M * N) time, O(1) space.
# Use first row and first column as indicators for zeroing the resto
def zero_matrix(m):
    M = len(m)
    N = len(m[0])
    first_row_zero, first_col_zero = False, False
    # Check row and column
    for i in range(M):
        if m[i][0] == 0:
            first_col_zero = True
            break

    for j in range(N):
        if m[0][j] == 0:
            first_row_zero = True
            break

    for i in range(1, M):
        for j in range(1, N):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0

    # Nullify based on indicators
    for i in range(1, M):
        if m[i][0] == 0:
            nullify_row(m, i)

    for j in range(1, N):
        if m[0][j] == 0:
            nullify_col(m, j)

    # Now nullify first row and col
    if first_col_zero:
        nullify_col(m, 0)

    if first_row_zero:
        nullify_row(m, 0)

    return m
        

def nullify_row(m, i):
    N = len(m[0])
    for j in range(N):
        m[i][j] = 0


def nullify_col(m, j):
    M = len(m)
    for i in range(M):
        m[i][j] = 0


if __name__ == '__main__':
    result = zero_matrix_extramem(deepcopy(TEST_INPUT))
    assert check_result(result)

    result = zero_matrix(deepcopy(TEST_INPUT))
    assert check_result(result)