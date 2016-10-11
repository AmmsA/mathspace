import sys


def get_solution(matrix):
    """
    get final solution of problem given input matrix
    :param matrix: input matrix
    :return: path with min cost
    """
    rows = matrix.splitlines()
    for idx, row in enumerate(rows):
        rows[idx] = row.split()
        for idx2, val in enumerate(rows[idx]):
            rows[idx][idx2] = int(val, 16)

    memo = [[None for i in range(len(rows[0]))] for j in range(len(rows))]
    min_cost(rows, len(rows)-1, len(rows[0])-1, memo)
    return find_min_path(memo)


def min_cost(cost_matrix, m, n, memo):
    """
    DP Recursive function to determine the minimum cost of the matrix
    :param cost_matrix: The cost matrix
    :param m:
    :param n:
    :param memo: memoization matrix
    :return: Min path value at index m, n
    """
    if n < 0 or m < 0:
        return sys.maxint
    elif memo[m][n]:
        return memo[m][n]
    elif m == 0 and n == 0:
        return cost_matrix[m][n]
    else:
        value = cost_matrix[m][n] + min(min_cost(cost_matrix, m-1, n, memo),
                                        min_cost(cost_matrix, m, n-1, memo))
        memo[m][n] = value
        return value


def find_min_path(memo):
    """
    Find the path with the minimum cost
    :param memo: Memoization matrix
    :return: path as a String
    """
    path = ''
    i = len(memo) - 1
    j = len(memo[0]) - 1

    while True:
        if i == 0 and j == 0:
            break

        if i == 0:
            j -= 1
            path += 'r,'
        elif j == 0:
            i -= 1
            path += 'd,'
        elif memo[i-1][j] < memo[i][j-1]:
            i -= 1
            path += 'd,'
        elif memo[i-1][j] > memo[i][j-1]:
            j -= 1
            path += 'r,'

    return "%s" % path[::-1][1:]

