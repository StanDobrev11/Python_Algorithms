from collections import deque

string = input().split()

size = [0] * len(string)
prev = [0] * len(string)

best_size = 0
best_idx = 0

for idx in range(len(string)):
    current_str = string[idx]
    current_size = 1
    parent = None
    for prev_idx in range(idx - 1, -1, -1):
        prev_str = string[prev_idx]

        if len(prev_str) >= len(current_str):
            continue

        if size[prev_idx] + 1 >= current_size:  # for leftmost chain, else remove =
            current_size = size[prev_idx] + 1
            parent = prev_idx

    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

path = deque()
idx = best_idx

while idx is not None:
    path.appendleft(string[idx])
    idx = prev[idx]

print(*path)