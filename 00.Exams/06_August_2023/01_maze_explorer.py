n = int(input())

maze = []
for _ in range(n):
    maze.append(list(input()))


# for row in maze:
#     print(row)


def find_path(row, col, maze, counter, min_size):
    if row not in range(len(maze)) or col not in range(len(maze[0])):
        return
    if maze[row][col] == '#':
        return
    if maze[row][col] == 'v':
        return
    if maze[row][col] == 'E':
        # counter += 1
        min_size.append(counter)
        return
    maze[row][col] = 'v'
    counter += 1

    find_path(row - 1, col, maze, counter, min_size)
    find_path(row + 1, col, maze, counter, min_size)
    find_path(row, col - 1, maze, counter, min_size)
    find_path(row, col + 1, maze, counter, min_size)

    maze[row][col] = '.'
    counter -= 1

    return min_size


counter = 0
min_size = []

print(min(find_path(0, 0, maze, counter, min_size)))
