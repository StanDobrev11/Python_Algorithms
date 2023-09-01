first_timeline = input().split()
second_timeline = input().split()

rows = len(second_timeline) + 1
cols = len(first_timeline) + 1

dp = [([0] * cols) for _ in range(rows)]
parent = []
best = 0
for row in range(1, rows):
    for col in range(1, cols):
        if second_timeline[row - 1] == first_timeline[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        if dp[row][col] > best:
            best = dp[row][col]
            parent.append(second_timeline[row - 1])


# for row in dp:
    # print(row)
print(*parent)
print(dp[rows - 1][cols - 1])