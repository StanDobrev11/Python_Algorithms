permutation = [int(x) for x in input().split()]

ordered = [x for x in range(1, len(permutation) + 1)]

# print(permutation)
# print(ordered)

rows = len(permutation) + 1
cols = len(ordered) + 1

dp = [([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if permutation[row - 1] == ordered[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(f'Maximum pairs connected: {dp[rows - 1][cols - 1]}')

# for row in dp:
#     print(row)
