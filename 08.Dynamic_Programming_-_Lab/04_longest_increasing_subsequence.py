nums = [int(x) for x in input().split()]

size = [0] * len(nums)
parent = [None] * len(nums)

size[0] = 1
best_idx = 0
best_size = 1

for current in range(1, len(nums)):
    current_num = nums[current]
    current_best = 1
    current_parent = None
    for prev in range(current - 1, -1, -1):
        prev_num = nums[prev]
        if prev_num >= current_num:
            continue
        if size[prev] + 1 >= current_best:
            current_best = size[prev] + 1
            current_parent = prev

    size[current] = current_best
    parent[current] = current_parent

    if current_best > best_size:
        best_size = current_best
        best_idx = current

# print(best_size)

result = []

while best_idx is not None:
    result.append(nums[best_idx])
    best_idx = parent[best_idx]

result.reverse()
print(*result)
