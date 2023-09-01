def dfs(key, row, col, matrix):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])):
        return
    if matrix[row][col] == 'v':
        return
    if matrix[row][col] != key:
        return
    matrix[row][col] = 'v'
    dfs(key, row + 1, col, matrix)
    dfs(key, row - 1, col, matrix)
    dfs(key, row, col + 1, matrix)
    dfs(key, row, col - 1, matrix)


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

area = {}
for row in range(rows):
    for col in range(cols):
        current_key = matrix[row][col]
        if current_key == 'v':
            continue

        dfs(current_key, row, col, matrix)
        if current_key not in area:
            area[current_key] = 1
        else:
            area[current_key] += 1

area_count = 0
for value in area.values():
    area_count += value
print(f"Areas: {area_count}")
for letter, value in sorted(area.items()):
    print(f"Letter '{letter}' -> {value}")
