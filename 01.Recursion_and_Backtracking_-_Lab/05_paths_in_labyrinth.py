def check_valid(row, col, lab):
    if row not in range(0, len(lab)) or col not in range(0, len(lab[0])):
        return False
    if lab[row][col] == "*":
        return False
    if lab[row][col] == "v":
        return False
    return True


def find_path(row, col, lab, direction, path):
    if check_valid(row, col, lab):
        if lab[row][col] == 'e':
            path.append(direction)
            print(*path, sep="")
            path.pop()
            return
        else:
            lab[row][col] = 'v'
            path.append(direction)

            find_path(row - 1, col, lab, "U", path)
            find_path(row + 1, col, lab, "D", path)
            find_path(row, col - 1, lab, "L", path)
            find_path(row, col + 1, lab, "R", path)

            path.pop()
            lab[row][col] = '-'


rows = int(input())
cols = int(input())

lab = []
for _ in range(rows):
    lab.append(list(input()))

find_path(0, 0, lab, "", list())
