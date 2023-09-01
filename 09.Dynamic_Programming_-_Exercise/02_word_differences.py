# original_str = input()
# modified_str = input()
#
# matrix = [[None] * (len(original_str) + 1) for _ in range(len(modified_str) + 1)]
#
# # for row in matrix:
# #     print(row)
#
# count = 0
# # for row in range(len(modified_str)):
# #     for col in range(len(original_str)):
# #         if modified_str[col] == original_str[row]:
# #             continue
# #         else:
# #             count += 1
#
# for idx, symbol in enumerate(original_str):
#     if symbol == modified_str[idx]:
#         continue
#     else:
#         count += 1
#
#
#
# print(count * 2)

first = input()
second = input()

dp = []
rows = len(first) + 1
cols = len(second) + 1

for _ in range(rows):
    dp.append([0] * cols)

for col in range(1, cols):
    dp[0][col] = col  # dp[0][col - 1] + 1
for row in range(1, rows):
    dp[row][0] = row

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1

# for row in dp:
#     print(row)
print(f'Deletions and Insertions: {dp[rows - 1][cols - 1]}')
