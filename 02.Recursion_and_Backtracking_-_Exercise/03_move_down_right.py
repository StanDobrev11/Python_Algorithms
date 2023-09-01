def is_valid(row, col):
    if row not in range(len(maze)):
        return False
    if col not in range(len(maze[0])):
        return False
    return True


def find_path(maze, row, col, count):
    if is_valid(row, col):

        if maze[row][col] == 'exit':
            count.append(1)
            # print(len(count))
            return

        find_path(maze, row + 1, col, count)
        find_path(maze, row, col + 1, count)

        return len(count)


rows = int(input())
cols = int(input())

maze = [['' for _ in range(cols)] for _ in range(rows)]

maze[-1][-1] = 'exit'
# print(len(maze))
# print(len(maze[0]))

print(find_path(maze, 0, 0, list()))
