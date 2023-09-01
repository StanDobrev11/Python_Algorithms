def check_true_false(exprs):
    if exprs[0] == 't':
        return exprs[2]
    else:
        return exprs[4]


line = input().split()

while len(line) > 1:
    half_idx = len(line) // 2
    exprs = line[half_idx - 2:half_idx + 3]
    for _ in range(5):
        line.pop(half_idx - 2)

    line.insert(half_idx - 2, check_true_false(exprs))

print(*line)

