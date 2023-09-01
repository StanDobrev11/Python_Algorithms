def draw_star(n):
    if n == 0:
        return
    print('*' * n)
    draw_star(n - 1)
    print('#' * n)


n = int(input())

draw_star(n)





# def draw_figure(n):
#     draw_star(n)
#     draw_hash(n, 1)
#
#
# def draw_star(n):
#     if n == 0:
#         return '*'
#     print('*' * n)
#     draw_star(n - 1)
#
#
# def draw_hash(n, x):
#     if x == n + 1:
#         return '#' * n
#     print('#' * x)
#     draw_hash(n, x + 1)
#
#
# n = int(input())
#
# draw_figure(n)
