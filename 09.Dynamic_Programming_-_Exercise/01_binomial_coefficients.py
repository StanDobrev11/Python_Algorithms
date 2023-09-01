from math import factorial


def binomial_coefficient(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


def find_bionminal_coef(row, col, rows, cols, matrix):
    for row in range(2, rows + 1):
        for col in range(1, cols + 1):
            if matrix[row][col] == 0:
                break
            matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]


def calc_binom(n, k, memo):
    if f'{n} {k}' in memo:
        return memo[f'{n} {k}']
    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n - 1, k - 1, memo) + calc_binom(n - 1, k, memo)
    memo[f'{n} {k}'] = result
    return result


n = int(input())
k = int(input())

# matrix = [[None] * (k + 1) for _ in range(n + 1)]
#
# for row in range(n + 1):
#     for col in range(k + 1):
#         if row >= col:
#             matrix[row][col] = 1
#         else:
#             matrix[row][col] = 0
#
# rows = n
# cols = k


# for row in matrix:
#     print(row)


#
# find_bionminal_coef(0, 0, rows, cols, matrix)
# print(matrix[n][k])
#


print(calc_binom(n, k, {}))
