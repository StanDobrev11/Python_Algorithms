def print_board(board):
    for row in board:
        print(" ".join(row))


def remove_queen(row, col, board, horizontal, vertical, left_diag, right_diag):
    board[row][col] = '-'
    horizontal.remove(row)
    vertical.remove(col)
    left_diag.remove(col - row)
    right_diag.remove(col + row)


def set_queen(row, col, board, horizontal, vertical, left_diag, right_diag):
    board[row][col] = "*"
    horizontal.add(row)
    vertical.add(col)
    left_diag.add(col - row)
    right_diag.add(col + row)


def can_place_queen(row, col, horizontal, vertical, left_diag, right_diag):
    if row in horizontal:
        return False
    if col in vertical:
        return False
    if (col - row) in left_diag:
        return False
    if (col + row) in right_diag:
        return False
    return True


def put_queen(row, board, horizontal, vertical, left_diag, right_diag):
    if row == 8:
        print_board(board)
        print()
        return

    for col in range(8):
        if can_place_queen(row, col, horizontal, vertical, left_diag, right_diag):
            set_queen(row, col, board, horizontal, vertical, left_diag, right_diag)
            put_queen(row + 1, board, horizontal, vertical, left_diag, right_diag)
            remove_queen(row, col, board, horizontal, vertical, left_diag, right_diag)


board = [['-' for col in range(8)] for row in range(8)]

put_queen(0, board, set(), set(), set(), set())
